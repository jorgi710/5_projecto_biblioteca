from django import forms
from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    """Form definition for Autor."""

    class Meta:
        """Meta definition for Autorform."""

        model = Autor
        fields = ('nombre', 'apellido', 'nacionalidad', 'descripcion')


class LibroForm(forms.ModelForm):
    """Form definition for Libro."""

    class Meta:
        """Meta definition for Libroform."""

        model = Libro
        fields = ('titulo')

