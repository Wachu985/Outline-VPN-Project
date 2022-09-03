from django.shortcuts import render

from .models import Producto,Principal,FAQ
from django.views.generic import TemplateView,ListView

# Create your views here.


class Home(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["presentacion"] = Principal.objects.latest('created')
        return context
    


class Productos(ListView):
    template_name = "home/productos.html"
    model = Producto



class FAQ(ListView):
    template_name = "home/faq.html"
    model = FAQ

