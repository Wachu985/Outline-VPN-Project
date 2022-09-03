import requests
from requests.exceptions import ConnectionError,ConnectTimeout
#
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import FormView,ListView,DeleteView,DetailView,UpdateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

#
from .forms import CreateKeyForm,CreateServerForm,RenameKeyForm,ChangeCuotaForm
from .models import OutlineKey,OutlineServer
from .contants import *

#App de Terceros
from outline_vpn.outline_vpn import OutlineVPN

# Create your views here.
"""Vista de la Creacion de la Llave"""
class CreateKeyView(LoginRequiredMixin,FormView):
    template_name = 'ovpn/create_key.html'
    form_class = CreateKeyForm
    success_url = reverse_lazy('user_app:user_panel')
    login_url = reverse_lazy('user_app:user_login')

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(
                reverse(
                    'home_app:home'
                )
            ) 
        return super(CreateKeyView,self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        usuario = form.cleaned_data['user']
        server = form.cleaned_data['server']
        limit_data = form.cleaned_data['limit_data']
        try:
            requests.get(server.api_url,verify=False,timeout=6)
        except ConnectionError or ConnectTimeout:
            return HttpResponseRedirect(
                reverse(
                    'ovpn_app:error'
                )
            )
        OutlineKey.objects.create_key(usuario,server,limit_data)
        return super(CreateKeyView, self).form_valid(form)

"""Vista de la Creacion de Servidor"""
class CreateServerView(LoginRequiredMixin,FormView):
    template_name = 'ovpn/create_server.html'
    form_class = CreateServerForm
    success_url = reverse_lazy('user_app:user_panel')
    login_url = reverse_lazy('user_app:user_login')

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(
                reverse(
                    'home_app:home'
                )
            ) 
        return super(CreateServerView,self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        api_url = form.cleaned_data['api_url']
        server_name = form.cleaned_data['server_name']
        limit_bytes = form.cleaned_data['limit_bytes']
        user = self.request.user
        try:
            requests.get(api_url,verify=False,timeout=6)
        except ConnectionError or ConnectTimeout:
            return HttpResponseRedirect(
                reverse(
                    'ovpn_app:error'
                )
            )
        OutlineServer.objects.create_server(api_url,server_name,limit_bytes,user)
        return super(CreateServerView, self).form_valid(form)


class ServersListView(LoginRequiredMixin,ListView):
    model = OutlineServer
    template_name = "ovpn/list_server.html"
    login_url = reverse_lazy('user_app:user_login')

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(
                reverse(
                    'home_app:home'
                )
            ) 
        return super(ServersListView,self).render_to_response(context, **response_kwargs)

    def get_queryset(self):
        user = self.request.user
        return OutlineServer.objects.list_servers(user)



class ServerDeleteView(LoginRequiredMixin,DeleteView):
    model = OutlineServer
    template_name = 'ovpn/delete_server.html'
    success_url = reverse_lazy('ovpn_app:list_server')
    login_url = reverse_lazy('user_app:user_login')


    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(
                reverse(
                    'home_app:home'
                )
            ) 
        return super(ServerDeleteView,self).render_to_response(context, **response_kwargs)



class OutlineKeyDetailView(LoginRequiredMixin,DetailView):
    model = OutlineKey
    template_name = "ovpn/key_detail.html"
    login_url = reverse_lazy('user_app:user_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        key = OutlineKey.objects.get(id=pk)
        user = key.user
        try:
            key_id = user.outlinekey.key_id
            api_url = user.outlinekey.server.api_url
        except:
            return context
        try:
            requests.get(api_url,verify=False,timeout=5)
        except ConnectionError or ConnectTimeout:
            context["server_error"] = 'Error al Conectarse con el Servidor. Por Favor Contacte con el Administrador'
            return context
        client = OutlineVPN(api_url=api_url)
        llaves = client.get_keys()
        for llave in llaves:
            if llave.key_id == str(key_id):
                if llave.used_bytes:
                    if user.outlinekey:
                        used_bytes = conversor(llave.used_bytes).split('-')
                        
                        OutlineKey.objects.save_used_bytes(user.outlinekey.id,used_bytes)
                    context["used_bytes"] = used_bytes[1]
                else:
                    if user.outlinekey:
                        OutlineKey.objects.save_used_bytes(user.outlinekey.id,0)
                    context["used_bytes"] = 'B'
                return context
        return context
    

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(
                reverse(
                    'home_app:home'
                )
            ) 
        return super(OutlineKeyDetailView,self).render_to_response(context, **response_kwargs)


class OutlineKeyDeleteView(LoginRequiredMixin,DeleteView):
    model = OutlineKey
    template_name = "ovpn/delete_key.html"
    success_url = reverse_lazy('ovpn_app:list_server')
    login_url = reverse_lazy('user_app:user_login')

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(
                reverse(
                    'home_app:home'
                )
            ) 
        return super(OutlineKeyDeleteView,self).render_to_response(context, **response_kwargs)


class RenameKeyUpdateView(LoginRequiredMixin,UpdateView):
    form_class = RenameKeyForm
    model = OutlineKey
    template_name = "ovpn/rename_key.html"
    success_url = reverse_lazy('ovpn_app:list_server')
    login_url = reverse_lazy('user_app:user_login')


    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(
                reverse(
                    'home_app:home'
                )
            ) 
        return super(RenameKeyUpdateView,self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        pk = self.kwargs['pk']
        name = form.cleaned_data['name']
        user = OutlineKey.objects.get(id=int(pk))
        api_url = user.server.api_url
        try:
            requests.get(api_url,verify=False,timeout=6)
        except ConnectionError or ConnectTimeout:
            return HttpResponseRedirect(
                reverse(
                    'ovpn_app:error'
                )
            )
        client = OutlineVPN(api_url=api_url)
        client.rename_key(int(user.key_id),name)
        return super(RenameKeyUpdateView, self).form_valid(form)


class ChangeCuotaUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ChangeCuotaForm
    model = OutlineKey
    template_name = "ovpn/change_cuota.html"
    success_url = reverse_lazy('ovpn_app:list_server')
    login_url = reverse_lazy('user_app:user_login')


    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(
                reverse(
                    'home_app:home'
                )
            ) 
        return super(ChangeCuotaUpdateView,self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        pk = self.kwargs['pk']
        limit_data = form.cleaned_data['limit_data']
        user = OutlineKey.objects.get(id=int(pk))
        api_url = user.server.api_url
        client = OutlineVPN(api_url=api_url)
        try:
            requests.get(api_url,verify=False,timeout=6)
        except ConnectionError or ConnectTimeout:
            return HttpResponseRedirect(
                reverse(
                    'ovpn_app:error'
                )
            ) 
        client.delete_data_limit(int(user.key_id))
        client.add_data_limit(int(user.key_id),int(limit_data)*CONVERT_GB)
        return super(ChangeCuotaUpdateView, self).form_valid(form)



class ErrorView(TemplateView):
    template_name = "home/error.html"
