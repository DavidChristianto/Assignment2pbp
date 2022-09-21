from django.shortcuts import render
from mywatchlist.models import mywatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_watchlist_item = mywatchlist.objects.all()
    counter = 0
    for x in data_watchlist_item:
        if("YES" == x.watched):
            counter += 1
    if(counter>4):
        message = "Congratulations, you have watched movies a lot!"
    else:
        message = "Woah, you have not much watched movies!"

    context = {
        'list_item': data_watchlist_item,
        'name': 'By David Christianto',
        'npm': '2106720866',
        'watch_message': message,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request,id):
    data = mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")