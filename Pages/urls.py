from django.urls import path
from Pages import views

urlpatterns = [
    path('', views.posteos, name = 'Posteos'),
    path('post/<int:pk>', views.posteos_n, name = 'Posteos_n'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]