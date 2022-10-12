from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from todolist.models import Task
from django.shortcuts import redirect
from django.urls import reverse
@login_required(login_url='/todolist/login/')

# Create your views here.
def show_todolist(request):
    # data_todolist_item = Task.objects.filter(user=request.user)
    context = {
        'name_of_user': request.user,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def show_xml(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = Task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request,id):
    data = Task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url="/todolist/login/")
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/todolist/login/")
def create_task(request):
    if request.method == "POST":
        Field_title = request.POST.get("title")
        description = request.POST.get("description")
        answer = HttpResponseRedirect(reverse("todolist:show_todolist"))
        Task.objects.create(date=datetime.datetime.today(), title= Field_title, description=description, user=request.user,)
        return answer
    return render(request, "create_task.html")

@login_required(login_url="/todolist/login/")
def update_task_status(request, selected_id):
    selected_task = Task.objects.get(user=request.user, id=selected_id)
    answer = HttpResponseRedirect(reverse("todolist:show_todolist"))
    selected_task.is_finished = not selected_task.is_finished
    selected_task.save(update_fields=["is_finished"])

    return answer

@login_required(login_url="/todolist/login/")
def remove_task(request, selected_id):
    answer = HttpResponseRedirect(reverse("todolist:show_todolist"))
    selected_task = Task.objects.get(user=request.user, id=selected_id)
    selected_task.delete()
    return answer

