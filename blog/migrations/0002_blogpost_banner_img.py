# Generated by Django 5.0.4 on 2024-09-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='banner_img',
            field=models.ImageField(blank=True, null=True, upload_to='banners/'),
        ),
    ]
