from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.GroupCreate.as_view(), name='create-room'),
    path('enter/', views.GroupEnterView.as_view(), name='enter-room'),
    path('<str:room_name>/', views.room, name='room'),
    
]