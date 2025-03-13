from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_landing_view, name='blog_landing'),
]