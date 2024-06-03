from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('<int:blog_id>/', views.add_comment, name='post_comment'),
    path('<int:user_id>/', views.logout, name='logout'),
    path('<int:blog_id>/<int:user_id>/like/', views.add_like, name='post_like'),
    path('<int:blog_id>/<int:user_id>/dislike/', views.add_dislike, name='post_dislike'),
    path('register/', views.register, name='register')
 
]