from django.urls import path
from . import views

urlpatterns = [
    path('business-stats/<int:pk>/', views.GetBusinessStats.as_view(), name='kpi_detail'),
]