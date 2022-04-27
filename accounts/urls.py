from django.urls import path

app_name = 'accounts'

from . import  views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.AddUserCreateView.as_view(), name='add_user'),
    path('perfil/', views.create_profile, name='create_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
]