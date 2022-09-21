from django.urls import path
from .views import BibliotecaHome, CrearAutor

app_name = 'biblioteca'

urlpatterns = [ 
    path('', BibliotecaHome.as_view(), name='home'),
    path('crear_autor/', CrearAutor.as_view(), name='crear_autor')
]