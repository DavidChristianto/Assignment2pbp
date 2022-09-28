from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
# buat function show_katalog
def show_katalog(request):
    # dpt dr models.py
    #variabel untuk ambil semua data/object di models.py
    data_katalog_item = CatalogItem.objects.all()
    context = { # data yg akan digunakan ditemplate dalam sebuah dict
        'list_item': data_katalog_item,
        'name': 'David',
        'npm': '2106720866'
    }
    # pake function render untuk request dan naro nama tempat template,dan contekk untuk masukin data ke template
    return render(request, "katalog.html", context) 