# Generated by Django 3.0.6 on 2020-06-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventurethriller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventurethrillermovie',
            name='free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='adventurethrillermovie',
            name='member_required',
            field=models.BooleanField(default=False),
        ),
    ]
