from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('',views.getData), 
    path('add/', views.addUser),
    path('update/', views.updateData),
    path('delete/', views.deleteUser),
    path('list/', views.UserList.as_view()),
    path('list/<uuid:user_id_text>', views.UserDetail.as_view()),
    path('post-list/', views.PostList.as_view()),
    path('post-list/<uuid:post_id_text>', views.DeletePost.as_view()),
    path('post-like/', views.LikeUnlikePost.as_view()),
   # path('follower-list/', views.FollowerList.as_view()),
    path('follower-add-remove/', views.AddRemoveFollower.as_view()),
    path('followers/<uuid:user_id_text>/', views.Followers.as_view(), name='followers'),
    path('comments/', views.Comments.as_view()),
    path('comments/<uuid:comment_id_text>', views.commentDelete.as_view()),
    path('commentlike/', views.LikeUnlikeComment.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)