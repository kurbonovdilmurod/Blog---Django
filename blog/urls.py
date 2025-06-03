from django.urls import path
from blog import views

urlpatterns = [
    path('<slug:slug>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]
