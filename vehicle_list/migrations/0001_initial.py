# Generated by Django 4.0.2 on 2022-02-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=500)),
                ('speed', models.CharField(max_length=500)),
                ('average_speed', models.CharField(max_length=500)),
                ('engine_status', models.CharField(max_length=500)),
                ('fuel_level', models.CharField(max_length=500)),
                ('temperature', models.CharField(max_length=500)),
                ('on_off', models.CharField(max_length=500)),
            ],
        ),
    ]
