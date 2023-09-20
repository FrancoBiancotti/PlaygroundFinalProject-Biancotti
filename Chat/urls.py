from django.urls import path
from Chat import views

urlpatterns = [
    path('', views.chats, name = 'Chats'),
    path('Chats_n/<int:pk>', views.chats_n, name = 'Chats_n'),
]