from django.urls import path
from . import views


urlpatterns = [
    path('', views.management_landing_view, name='management_landing'),
    path('blog/', views.management_blog_view, name='blog_management'),
    path('blog/add_post', views.management_blog_add_post_view, name='blog_add_post'),
    path('storefront/', views.management_storefront_view, name='storefront_management'),
    path('announcements/', views.management_announcements_view, name='announcements_management'),
    path('newsletter/', views.management_newsletter_view, name='newsletter_management')
]