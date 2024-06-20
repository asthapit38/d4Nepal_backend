from django.urls import path
from . import views

urlpatterns = [
    path('', views.BusinessTypeList.as_view(), name='business-type-list'),
    path('create/', views.BusinessTypeCreate.as_view(), name='business-type-create'),
    path('show/<int:id>/', views.BusinessTypeRetrieve.as_view(), name='business-type-retrieve'),
]
