from django.contrib import admin
from plan.models import Plan
from business_profile.models import BusinessProfile
from subscriptions.models import Subscription


# Register your models here.
admin.site.register(Plan)
admin.site.register(BusinessProfile)
admin.site.register(Subscription)