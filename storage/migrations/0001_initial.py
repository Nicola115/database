# Generated by Django 2.2 on 2021-06-11 06:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('cost', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('number', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
            ],
        ),
    ]
