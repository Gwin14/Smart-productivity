from . import models
from django import forms


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
