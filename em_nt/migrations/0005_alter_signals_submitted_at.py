# Generated by Django 5.1 on 2024-08-20 06:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('em_nt', '0004_signals_submitted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signals',
            name='submitted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
