from django import forms

from .models import OutlineKey, OutlineServer

class CreateKeyForm(forms.ModelForm):

    class Meta:

        model = OutlineKey
        fields = (
            'limit_data',
            'user',
            'server'
        )
        widgets = {
            'limit_data': forms.NumberInput(
                attrs={
                    'placeholder':'Inserte la Cuota',
                    'class':'form-control',
                    'id':'floatingPassword'
                }
            ),
            'user': forms.Select(
                attrs={
                    'class':'form-select selectiones'
                }
            ),
            'server': forms.Select(
                attrs={
                    'class':'form-select selectiones'
                }
            ),
        }


class CreateServerForm(forms.ModelForm):

    class Meta:

        model = OutlineServer
        fields = (
            'api_url',
            'server_name',
            'limit_bytes',
        )
        widgets = {
            'api_url': forms.TextInput(
                attrs={
                    'placeholder':'Api URL',
                    'class':'form-control',
                    'id':'floatingPassword'
                }
            ),
            'server_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'floatingPassword'
                }
            ),
            'limit_bytes': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'floatingPassword'
                }
            ),
        }


class RenameKeyForm(forms.ModelForm):
    class Meta:

        model = OutlineKey
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Nombre',
                    'class':'form-control',
                    'id':'floatingPassword'
                }
            ),
        }


class ChangeCuotaForm(forms.ModelForm):
    class Meta:

        model = OutlineKey
        fields = (
            'limit_data',
        )
        widgets = {
            'limit_data': forms.TextInput(
                attrs={
                    'placeholder':'Cuota Total',
                    'class':'form-control',
                    'id':'floatingPassword'
                }
            ),
        }