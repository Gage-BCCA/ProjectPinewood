from django.urls import path
from . import views


urlpatterns = [
    path('', views.management_landing_view, name='management_landing'),

    #=================================
    # Blog URLs
    #=================================
    path('blog/', views.blog_overview, name='blog_management'),
    path('blog/create', views.add_post_view, name='add_post'),
    path('blog/delete', views.delete_post_view, name='delete_post'),
    path('blog/edit', views.edit_post_view, name='edit_post'),
    path('blog/all', views.all_posts_view, name='all_posts'),



    #=================================
    # Storefront URLs
    #=================================
    path('storefront/', views.storefront_overview, name='storefront_management'),
    path('storefront/add', views.add_featured_product_view, name='add_featured_product'),
    path('storefront/remove', views.remove_featured_product_view, name='remove_featured_product'),
    path('storefront/all', views.all_featured_products_view, name='all_featured_products'),
    path('storefront/edit', views.edit_featured_product_view, name='edit_featured_product'),

    #=================================
    # Announcement URLs
    #=================================
    path('announcements/', views.announcements_overview, name='announcements_management'),
    path('announcements/create', views.create_announcement_view, name='create_announcement'),
    path('announcements/remove', views.remove_current_announcement_view, name='remove_announcement'),
    path('announcements/all', views.all_announcements_view, name='all_announcements'),
    path('announcements/edit', views.edit_announcement_view, name='edit_announcement'),

    #=================================
    # Newsletter URLs
    #=================================
    path('newsletter/', views.newsletter_overview, name='newsletter_management'),
    path('newsletter/add', views.add_email_view, name='add_email'),
    path('newsletter/remove', views.remove_email_view, name='remove_email'),
    path('newsletter/all', views.all_emails_view, name='all_emails'),


    #=================================
    # Gallery URLs
    #=================================
    path('gallery/', views.gallery_overview, name='gallery_management'),
    path('gallery/add', views.add_picture_view, name='add_picture'),
    path('gallery/remove', views.remove_picture_view, name='remove_picture'),
    path('gallery/all', views.all_pictures_view, name='all_pictures'),
    path('gallery/edit', views.edit_picture_view, name='edit_picture'),
]