# Generated by Django 4.2.5 on 2023-09-19 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheese', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Cheese',
        ),
    ]