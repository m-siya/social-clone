from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData), 
    path('add/', views.addUser),
    path('update/', views.updateData),
    path('delete/', views.deleteUser),
    path('list/', views.UserList.as_view()),
    path('detail/<uuid:uuid>', views.UserDetail.as_view())
]