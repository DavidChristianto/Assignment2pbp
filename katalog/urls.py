# TODO: Implement Routings Herefrom django.urls import path
from katalog.views import show_katalog
from django.urls import path

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    path('katalog/', include('katalog.urls')),
]