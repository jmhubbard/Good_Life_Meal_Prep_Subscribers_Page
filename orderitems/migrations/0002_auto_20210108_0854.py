# Generated by Django 3.1.5 on 2021-01-08 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderitems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='special_requests',
            field=models.TextField(blank=True),
        ),
    ]
