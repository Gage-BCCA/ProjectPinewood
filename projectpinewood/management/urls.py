from django.urls import path
from . import views


urlpatterns = [
    path('', views.management_landing_view, name='management_landing'),
    path('blog/', views.management_blog_view, name='blog_management'),
    path('blog/add_post', views.management_blog_add_post_view, name='blog_add_post'),
]