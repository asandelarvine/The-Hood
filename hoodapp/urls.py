from django.urls import path
# from django.contrib import admin
from .import views
# from . import views as app_views


urlpatterns = [
    path('',views.index ,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='index'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_hood',views.create_hood, name= 'create_hood'),
    path('hood/', views.hood, name = 'hood'),
    path('hood/<str:name>',views.one_hood,name='one_hood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),
    path('businesses/',views.businesses, name='businesses'),
    path('new_business/',views.new_business, name='new_business'),
    path('authorities/',views.authorities, name='authorities'),
    path('create_authorities/',views.create_authorities, name='create_authorities'),
    path('health',views.health, name='health'),
    path('post/', views.post, name = 'post'),
    path('create_post', views.create_post, name='create_post'),
    path('view/blog/(\d+)',views.view_blog,name='view_blog'),
    path('search/',views.search_results, name='search_results'),
    
    
]