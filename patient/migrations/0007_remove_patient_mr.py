# Generated by Django 2.2 on 2021-06-11 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_prescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='mr',
        ),
    ]