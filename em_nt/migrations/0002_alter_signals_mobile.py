# Generated by Django 4.1.13 on 2024-08-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('em_nt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signals',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
