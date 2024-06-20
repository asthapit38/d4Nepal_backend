from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    business_per_account = models.IntegerField(null=True, blank=True)
    has_unlimited_business = models.BooleanField(default=False)
    kpi = models.IntegerField(default=0)
    visual_graph = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
