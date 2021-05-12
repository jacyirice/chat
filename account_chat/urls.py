from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserUpdateView.as_view(), name='user-update'),
]