# Generated by Django 4.1.5 on 2023-01-28 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AndresMogollonApp', '0011_proyecto'),
    ]

    operations = [
        migrations.CreateModel(
            name='proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=250)),
                ('imagen', models.ImageField(upload_to='proyecto')),
                ('git', models.URLField(max_length=230)),
                ('host', models.URLField(max_length=230)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
            },
        ),
        migrations.DeleteModel(
            name='proyecto',
        ),
    ]
