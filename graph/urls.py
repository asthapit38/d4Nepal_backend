from django.urls import path
from . import views

urlpatterns = [
    path('', views.GraphListCreate.as_view(), name='graph-list-create'),
    path('<int:pk>/', views.GraphDeleteView.as_view(), name='graph-delete'),
    path('update/<int:pk>/', views.GraphUpdateView.as_view(), name='graph-update'),
]
