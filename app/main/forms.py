from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
#    role = forms.ChoiceField(choices=('Ученик', 'Учитель', 'Родитель'), required=True, help_text='Введите ваш статус')
#    last_name = forms.CharField(max_length=50, required=True, help_text='Введите вашу фамилию')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
