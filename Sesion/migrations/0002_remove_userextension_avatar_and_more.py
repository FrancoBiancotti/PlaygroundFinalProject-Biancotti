# Generated by Django 4.1.2 on 2023-09-17 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sesion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextension',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userextension',
            name='link',
        ),
    ]
