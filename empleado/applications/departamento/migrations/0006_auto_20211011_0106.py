# Generated by Django 3.2.8 on 2021-10-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0005_auto_20211010_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la Empresa'},
        ),
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]
