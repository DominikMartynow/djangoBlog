"""Wzoce URL dla blog_"""

from django.urls import path

from . import views

app_name = 'blog_'
urlpatterns = [
    #strona glowna
    path('', views.index, name='index'),

    #post
    path('<int:post_id>/', views.post, name='post'),

    #like    
    path('<int:post_id>/like/', views.like, name='like'),

    #profile uzytkowników
    path('users_list/', views.usersList, name='users_list'),

    #profil uzytkownika
    path('users_list/<int:user_id>/', views.userProfile, name='userProfile'),

    #usuwanie komentarza
    path('<int:post_id>/delete_comment>/<int:user_id>/', views.deleteComment, name='deleteComment'),

]