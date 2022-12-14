# Generated by Django 4.1.1 on 2022-09-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('nacionalidad', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autors',
                'ordering': ['nombre'],
            },
        ),
    ]
