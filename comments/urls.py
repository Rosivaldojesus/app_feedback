from django.urls import path

app_name = 'comments' 


from . import views 

urlpatterns = [
     path('profile/<slug:username>/', views.get_user_profile_or_add_comment, name='get_user_profile_or_add_comment'),
     path('details/<int:id_comment>/', views.comments_details, name='comments_details'),
     path('mark-unread/<int:id_comment>/', views.mark_unread, name='mark_unread'),
     path('comment-delete/<int:id_comment>/', views.comment_delete, name='comment_delete'),
     path('', views.comments_home, name='comments_home'),
]

