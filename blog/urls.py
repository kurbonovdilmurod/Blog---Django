from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('post/create/', views.create_blog, name="create_blog"),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('post/<slug:slug>/edit/', views.blog_edit, name="blog_edit"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]
