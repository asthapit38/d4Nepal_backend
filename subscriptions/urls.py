from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubscriptionListCreate.as_view(), name='subscription-list'),
    path('update/<int:pk>/', views.SubscriptionUpdateView.as_view(), name='subscription-update'),
    path('<int:pk>/', views.SubscriptionDeleteView.as_view(), name='subscription-delete'),
]
