from django.db import models
from kpi.models import Kpi
from graph.models import Graph


class BusinessType(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    kpi = models.ManyToManyField(Kpi, related_name='business_types')
    graph = models.ManyToManyField(Graph, related_name='business_types')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
