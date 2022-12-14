# Generated by Django 4.1.1 on 2022-09-15 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de pulicación')),
                ('autor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]
