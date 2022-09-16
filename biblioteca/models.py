from django.db import models

# Create your models here.

class Autor(models.Model):
    """Model definition for Autor."""

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 150)
    apellido = models.CharField(max_length = 150)
    nacionalidad = models.CharField(max_length = 150)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField('Fecha de pulicación', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autors'
        ordering = ["nombre"]
        
    def __str__(self):
        """Unicode representation of Autor."""
        return self.nombre + " " + self.apellido

class Libro(models.Model):
    """Model definition for Libro."""

    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length = 150, blank=False, null=False)
    disponbile = models.BooleanField(null=False, default=True)
    fecha_publicacion = models.DateField('Fecha de pulicación', auto_now=True, auto_now_add=False)
    

    # 1. Para indicar que la relacion que tiene con la identidad Autor es 1 - 1 seria:
    #autor_id = models.OneToOneField(Autor, on_delete=models.CASCADE)
    # 2. Que pasa si es de uno a mucho, es decir con una clave foranea. (Un autor puede tener varios libros)
    #autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    # 3. DIgamos que la relacion sea de muchos a muchos (UN libro puede tener muchos autores)
    autor_id = models.ManyToManyField(Autor)
    
    
    
    
    class Meta:
        """Meta definition for Libro."""

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ["titulo"]

    def __str__(self):
        """Unicode representation of Libro."""
        return self.titulo
