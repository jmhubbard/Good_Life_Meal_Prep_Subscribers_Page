# Generated by Django 3.1.5 on 2021-01-10 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_meal_picture_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='is_active',
            new_name='is_on_menu',
        ),
    ]