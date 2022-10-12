# TODO: Implement Routings Herefrom django.urls import path
from todolist.views import show_todolist, update_task_status
from todolist.views import show_xml #customize to the name of the function created
from todolist.views import show_json # adjust the name of the function created
from todolist.views import show_json_by_id #customise the name of the function created
from todolist.views import show_xml_by_id #customise the name of the function created
from django.urls import path
from todolist.views import register #customize with the name of the function created
from todolist.views import login_user #customize with the name of the function created
from todolist.views import logout_user #customize with the name of the function created
from todolist.views import create_task, remove_task, add

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('xml/', show_xml, name='show_xml'), #customize the name of the function created
    path('json/', show_json, name='show_json'), #customise the name of the function created
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #customise the name of the function created
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'), #customise the name of the function created
    path('register/', register, name='register'), #customize with the name of the function created
    path('login/', login_user, name='login'), #customize with the name of the function created
    path('logout/', logout_user, name='logout'), #customize with the name of the function created
    path('create-task/', create_task, name='create_task'),
    path("update-task-status/<int:selected_id>", update_task_status, name="update_task_status"),
    path("remove-task/<int:selected_id>", remove_task, name="remove_task"),
    path('add/', add, name='add'),
]
