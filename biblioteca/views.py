from django.shortcuts import render
from django.views.generic import View
from .forms import AutorForm

# Create your views here.


# Create your views here.

class BibliotecaHome(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'biblioteca_home.html', context)

class CrearAutor(View):
    
    def get(self, request, *args, **kwargs):
        context= {}
        return render(request, 'crear_autor.html', context)

    def post(self, request, *args, **kwargs):
        context= {}
        return render(request, 'crear_autor.html', context)