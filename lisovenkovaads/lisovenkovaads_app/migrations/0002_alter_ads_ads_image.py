# Generated by Django 4.1.7 on 2023-03-30 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lisovenkovaads_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='ads_image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]