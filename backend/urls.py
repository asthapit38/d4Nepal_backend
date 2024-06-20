
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),

    path('api/plans/', include('plan.urls')),
    path('api/business/', include('business_profile.urls')),
    path('api/subscriptions/', include('subscriptions.urls')),

    path('api/business-type/', include('business_type.urls')),
    path('api/kpi/', include('kpi.urls')),

    path('api/upload-data/', include('upload_data.urls')),
    path('api/', include('api.urls')),

]
