# Generated by Django 2.1.5 on 2019-05-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
