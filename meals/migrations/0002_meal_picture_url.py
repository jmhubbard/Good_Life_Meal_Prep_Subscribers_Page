# Generated by Django 3.1.5 on 2021-01-09 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='picture_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
