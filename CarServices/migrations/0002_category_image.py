# Generated by Django 4.0.4 on 2022-05-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarServices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/category'),
        ),
    ]
