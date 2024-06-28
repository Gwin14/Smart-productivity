from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from . import models


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
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',
                  'password1', 'password2', 'image')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este email já está em uso.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            profile, created = models.Profile.objects.get_or_create(user=user)
            if 'image' in self.cleaned_data:
                profile.image = self.cleaned_data['image']
                profile.save()
        return user
