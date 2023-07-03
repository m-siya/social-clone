from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.UserList.as_view()),
    path('<uuid:user_id_text>', views.UserDetail.as_view()),
    path('post-list/', views.PostList.as_view()),
    path('post-list/<uuid:post_id_text>', views.DeletePost.as_view()),
    path('post-like/', views.LikePost.as_view()),
    path('post-unlike/<post_likes_id_text>', views.UnlikePost.as_view()),
    path('repost/', views.MakeRepost.as_view()),
    path('repost/<uuid:repost_id_text>', views.DeleteRepost.as_view()),
   # path('follower-list/', views.FollowerList.as_view()),
    path('follower-add/', views.AddFollower.as_view()),
    path('follower-remove/<follower_id_text>', views.RemoveFollower.as_view()),
    path('followers/<uuid:user_id_text>/', views.Followers.as_view(), name='followers'),
    path('following/<uuid:user_id_text>/', views.Following.as_view(), name = 'following'),
    path('comments/', views.Comments.as_view()),
    path('comments/<uuid:comment_id_text>', views.commentDelete.as_view()),
    path('comment-like/', views.LikeComment.as_view()),
    path('comment-unlike/<uuid:comment_likes_id_text>', views.UnlikeComment.as_view()),
    path('tags/', views.Tags.as_view()),
    path('tags/<str:tag_name>/', views.DeleteTag.as_view()),
    path('tag-follow/', views.FollowTag.as_view()),
    path('tag-unfollow/<user_follows_tag_id_text>', views.UnfollowTag.as_view()),
    path('post-tag/', views.AddPostTag.as_view()),
    path('post-tag/<uuid:post_tag_id_text>', views.RemovePostTag.as_view()),
    path('post-tags/<uuid:post_id_text>', views.ViewPostTags.as_view()),
    path('comment-tag/', views.AddCommentTag.as_view()),
    path('comment-tag/<uuid:comment_tag_id_text>', views.RemoveCommentTag.as_view()),
    path('comment-tags/<uuid:comment_id_text>', views.ViewCommentTags.as_view()),
   # path('comments/<uuid:comment_id_text>', views.commentDelete.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)