# Generated by Django 4.1.1 on 2022-09-16 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.autor'),
        ),
    ]
