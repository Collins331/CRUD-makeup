# Generated by Django 5.1.3 on 2024-11-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='image',
            field=models.ImageField(upload_to='school/'),
        ),
    ]
