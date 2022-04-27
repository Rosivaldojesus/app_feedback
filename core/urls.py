from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.CoreView.as_view(), name='core_view' ),
]
