# Generated by Django 5.0.6 on 2024-06-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='business_per_account',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='has_unlimited_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plan',
            name='kpi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='visual_graph',
            field=models.IntegerField(default=0),
        ),
    ]
