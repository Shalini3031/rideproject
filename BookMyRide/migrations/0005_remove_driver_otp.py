# Generated by Django 4.2.14 on 2024-07-30 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookMyRide', '0004_rename_admin_id_admin_id_rename_driver_id_driver_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='otp',
        ),
    ]
