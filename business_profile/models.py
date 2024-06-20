from django.db import models
from django.contrib.auth.models import User
from business_type.models import BusinessType
from kpi.models import Kpi
from graph.models import Graph


class BusinessProfile(models.Model):
    objects = None
    name = models.CharField(max_length=100, unique=True)
    business_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    business_type = models.ForeignKey(BusinessType, on_delete=models.SET_NULL, null=True, blank=True)
    kpi = models.ManyToManyField(Kpi, related_name='business_profiles')
    graph = models.ManyToManyField(Graph, related_name='business_profiles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
