# Generated by Django 3.1.5 on 2021-01-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderitems', '0003_auto_20210108_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_on_current_menu',
            field=models.BooleanField(default=False),
        ),
    ]
