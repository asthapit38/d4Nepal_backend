# Generated by Django 5.0.6 on 2024-06-15 19:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business_profile', '0004_businessprofile_kpi_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantCSV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('month_no', models.IntegerField()),
                ('month_nm', models.CharField(max_length=12)),
                ('quarter', models.CharField(max_length=4)),
                ('year_month', models.IntegerField()),
                ('week', models.IntegerField()),
                ('week_ending_mon_sun_dt', models.DateTimeField()),
                ('min_order_datetime', models.DateTimeField()),
                ('kpi', models.CharField(max_length=255)),
                ('menu_category', models.CharField(max_length=255)),
                ('menu_group', models.CharField(max_length=255)),
                ('menu_item', models.CharField(max_length=255)),
                ('actual', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_profile.businessprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload_data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
