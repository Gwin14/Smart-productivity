from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class NoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title', 'content', 'tags', 'picture']

        labels = {
            'title': 'Título',
            'content': 'Conteúdo',
            'tags': 'Tags',
            'picture': 'Capa',
        }


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',
                  'password1', 'password2', 'image')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError(
                'Já existe esse email', code='invalid'))
