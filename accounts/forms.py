from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# UserLoginForm
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Қолданушының аты',
        widget=forms.TextInput(attrs={
            'placeholder': 'Қолданушының аты',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label='Құпия сөз',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Құпия сөз'
        })
    )


# UserForm
class UserForm(UserCreationForm):
    email = forms.EmailField(
        label='Электронды пошта',
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@gmail.com'
        })
    )
    username = forms.CharField(
        label='Қолданушының аты',
        widget=forms.TextInput(attrs={
            'placeholder': 'user.name'
        })
    )
    password1 = forms.CharField(
        label='Құпия сөз',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Қауіпсіз символдар жазыңыз!'
        })
    )
    password2 = forms.CharField(
        label='Құпия сөзді қайталау',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Құпия сөзді қайталау'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )


# ProfileUpdate
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name' )
