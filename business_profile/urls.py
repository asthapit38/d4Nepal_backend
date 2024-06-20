from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.BusinessProfileListCreate.as_view(), name='business_profile_list'),
    path('profile/update/<int:pk>/', views.BusinessProfileUpdate.as_view(), name='business_profile_update'),
    path('profile/<int:pk>/', views.BusinessProfileDelete.as_view(), name='business_profile_delete'),
]
