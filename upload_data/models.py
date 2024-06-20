from django.contrib.auth.models import User
from django.db import models
from business_profile.models import BusinessProfile


# Create your models here.
class UploadData(models.Model):
    file = models.FileField(upload_to='files/csv/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RestaurantCSV(models.Model):
    year = models.CharField(max_length=4)
    month_no = models.IntegerField()
    month_nm = models.CharField(max_length=12)
    quarter = models.CharField(max_length=4)
    year_month = models.CharField(max_length=128)
    week = models.CharField(max_length=4)
    week_ending_mon_sun_dt = models.DateField()
    min_order_datetime = models.DateField()
    kpi = models.CharField(max_length=255)
    menu_category = models.CharField(max_length=255)
    menu_group = models.CharField(max_length=255)
    menu_item = models.CharField(max_length=255)
    actual = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_profile = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
