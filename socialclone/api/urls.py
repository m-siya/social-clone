from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.getData), 
    path('add/', views.addUser),
    path('update/', views.updateData),
    path('delete/', views.deleteUser),
    path('list/', views.UserList.as_view()),
    path('list/<uuid:user_id_text>', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)