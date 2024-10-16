from django.urls import path
from . import views

app_name = 'inventory'


urlpatterns = [
    path('', views.home, name='home'),
    path('asset_list', views.asset_list, name='asset_list'),
    path('create/', views.asset_create, name='asset_create'),
    path('<int:pk>/update/', views.asset_update, name='asset_update'),
    path('<int:pk>/delete/', views.asset_delete, name='asset_delete'),
]