#
from django.urls import path

from . import views

app_name = "ovpn_app"

urlpatterns = [
    path(
        'panel/create_key/', 
        views.CreateKeyView.as_view(),
        name='create_key',
    ),
    path(
        'panel/create_server/', 
        views.CreateServerView.as_view(),
        name='create_server',
    ),
    path(
        'panel/list_server/', 
        views.ServersListView.as_view(),
        name='list_server',
    ),
    path(
        'panel/delete_server/<pk>/', 
        views.ServerDeleteView.as_view(),
        name='delete_server',
    ),
    path(
        'panel/detail_key/<pk>/', 
        views.OutlineKeyDetailView.as_view(),
        name='detail_key',
    ),
    path(
        'panel/delete_key/<pk>/', 
        views.OutlineKeyDeleteView.as_view(),
        name='delete_key',
    ),
    path(
        'panel/rename_key/<pk>/', 
        views.RenameKeyUpdateView.as_view(),
        name='rename_key',
    ),
    path(
        'panel/change_cuota/<pk>/', 
        views.ChangeCuotaUpdateView.as_view(),
        name='change_cuota',
    ),
    path(
        'error/', 
        views.ErrorView.as_view(),
        name='error',
    ),

]