# Generated by Django 5.2 on 2025-04-29 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_memberteetime_caddie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberteetime',
            name='caddie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caddie', to='app.caddie'),
        ),
    ]
