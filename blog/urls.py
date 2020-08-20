from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('new_post/', views.new_post, name='new_post'),
    path('<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('<slug:post_slug>/share/', views.post_share, name='post_share'),
    path('edit_post/<slug:post_slug>/', views.edit_post, name='edit_post'),
    path('delete_post/<slug:post_slug>/', views.delete_post, name='delete_post'),
]