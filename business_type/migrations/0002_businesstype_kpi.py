# Generated by Django 5.0.6 on 2024-06-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_type', '0001_initial'),
        ('kpi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstype',
            name='kpi',
            field=models.ManyToManyField(to='kpi.kpi'),
        ),
    ]
