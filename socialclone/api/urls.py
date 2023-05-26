from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData), 
    path('add/', views.addUser),
    path('update/', views.updateData),
    path('delete/', views.deleteUser)
]