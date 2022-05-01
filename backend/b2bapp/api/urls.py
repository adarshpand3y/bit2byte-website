from django.urls import path
from . import views

urlpatterns = [
    path('getblogs', views.getBlogs),
    path('getParticularBlog/<str:slug>', views.getParticularBlog),
    path('getHomeDetails', views.getHomeDetails),
]
