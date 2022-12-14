# Generated by Django 4.1.2 on 2022-10-19 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0003_alter_contitent_options_alter_country_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_flag',
            field=models.ImageField(blank=True, upload_to='photos/flags/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_photo',
            field=models.ImageField(blank=True, upload_to='photos/borders/%Y/%m/%d/'),
        ),
    ]
