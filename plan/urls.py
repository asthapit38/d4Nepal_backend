from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlanListCreate.as_view(), name='plan_list'),
    path('<int:pk>/', views.PlanDeleteView.as_view(), name='plan_delete'),
    path('update/<int:pk>/', views.PlanUpdateView.as_view(), name='plan_update'),
]
