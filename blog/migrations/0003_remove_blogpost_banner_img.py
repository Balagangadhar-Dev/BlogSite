# Generated by Django 5.0.4 on 2024-09-24 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_banner_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='banner_img',
        ),
    ]
