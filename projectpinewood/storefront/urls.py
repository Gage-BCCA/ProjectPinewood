from django.urls import path
from . import views


urlpatterns = [
    path('', views.store_landing_view, name='store_landing'),
]