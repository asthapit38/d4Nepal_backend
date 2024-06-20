from django.urls import path
from . import views

urlpatterns = [
    path('', views.KpiListCreate.as_view(), name='kpi-list-create'),
    path('<int:pk>/', views.KpiDeleteView.as_view(), name='kpi-delete'),
    path('update/<int:pk>/', views.KpiUpdateView.as_view(), name='kpi-update'),
]
