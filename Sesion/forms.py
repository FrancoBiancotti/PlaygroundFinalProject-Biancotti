from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User

'''
    FORMULARIO FormularioRegistro:
    - Username: str
    - Email: str
    - Password1: str
    - Password2: str
'''

class FormularioInicio(AuthenticationForm):

    username = AuthenticationForm().fields["username"]
    password = AuthenticationForm().fields["password"]

    # Cambiar los nombres de los campos a español
    username.label = "Nombre de Usuario"
    password.label = "Contraseña"


class FormularioRegistro(UserCreationForm):

    username  = forms.CharField(label='Nombre de usuario', required=True)
    email     = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

'''
    FORMULARIO FormularioEditarPerfil:
    - Email: str
    - First_name: str
    - Last_name: str
    - Descripcion: str
    - Link: str
    - Avatar: file
'''
class FormularioEditarPerfil(forms.Form):

    email       = forms.EmailField(required=True, widget=forms.EmailInput(attrs={ 'class' : 'form-control' }))
    first_name  = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }), label='Nombre')
    last_name   = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }), label='Apellido')
    descripcion = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={ 'class' : 'form-control' }))


'''
    FORMULARIO FormularioCambiarPassword:
    - Old_password: str
    - New_password1: str
    - New_password2: str
'''
class FormularioCambiarContraseña(PasswordChangeForm):

    old_password  = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Contraseña actual')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Contraseña nueva')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Confirmar contraseña nueva')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:'' for k in fields}