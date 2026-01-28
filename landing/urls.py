from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('delete-account/', views.delete_account, name='delete_account'),
]
