from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="post-detail"),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name="blogger-detail"),
    path('posts/new_post/', views.new_post, name="new_post"),
]
