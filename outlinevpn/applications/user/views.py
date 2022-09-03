from urllib import request
from requests.exceptions import ConnectionError,ConnectTimeout
import requests

#
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

#
from applications.ovpn.models import OutlineKey
from applications.ovpn.contants import conversor

#App de Terceros
from outline_vpn.outline_vpn import OutlineVPN

from django.views.generic import (
    View,
    CreateView,
    DetailView,
    ListView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
)
#
from .models import User


class UserRegisterView(LoginRequiredMixin,FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_app:user_login')
    login_url = reverse_lazy('user_app:user_login')
        
    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(
                reverse(
                    'home_app:home'
                )
            ) 
        return super(UserRegisterView,self).render_to_response(context, **response_kwargs)
    
    

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['password1'],
        )  
        # enviar el codigo al email del user
        return super(UserRegisterView, self).form_valid(form)



class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('user_app:user_panel')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'home_app:home'
            )
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('home_app:home')
    login_url = reverse_lazy('user_app:user_login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


class PanelListView(LoginRequiredMixin,ListView):
    model = User
    template_name = "users/panel.html"  
    login_url = reverse_lazy('user_app:user_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
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
      

    def get_queryset(self):
        id = self.request.user.id
        return User.objects.get_usuario(id)
    
