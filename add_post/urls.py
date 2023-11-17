from . import views
from django.urls import path,include

urlpatterns = [
    path('add/', views.addPost, name="add"),
    path('delete/', views.deletePost, name="delete"),
    path('search/', views.searchPost, name="search"),
    path('view/', views.viewPost, name="view"),
    path('viewAll/', views.viewAllPost, name="viewALL"),
]