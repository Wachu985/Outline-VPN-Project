#
from django.urls import path

from . import views

app_name = "user_app"

urlpatterns = [
    path(
        'panel/register/', 
        views.UserRegisterView.as_view(),
        name='user_register',
    ),
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='user_login',
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='user_logout',
    ),
    path(
        'panel/update/', 
        views.UpdatePasswordView.as_view(),
        name='user_update',
    ),
    path(
        'panel/', 
        views.PanelListView.as_view(),
        name='user_panel',
    ),
]