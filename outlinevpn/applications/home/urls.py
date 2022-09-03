#
from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.Home.as_view(),
        name='home',
    ),
    path(
        'productos/', 
        views.Productos.as_view(),
        name='productos',
    ),
    path(
        'faq/', 
        views.FAQ.as_view(),
        name='faq',
    ),
]