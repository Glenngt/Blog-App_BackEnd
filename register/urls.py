from . import views
from django.urls import path,include

urlpatterns = [
    path('add/', views.addUser, name="add"),
    path('delete/', views.deleteUser, name="delete"),
    path('search/', views.searchUser, name="search"),
    path('view/', views.viewUser, name="view")
]