# Generated by Django 4.0.2 on 2022-02-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_list', '0002_vehicle_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]