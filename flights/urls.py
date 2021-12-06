from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/', views.flight, name='flight'),
    path('<str:pk>/book/', views.book, name='book')
]
