# Generated by Django 2.1.5 on 2019-05-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20190529_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='meal',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
