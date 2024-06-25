from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=40,default='Título')
    content = models.TextField(blank=True, null=True,default='Conteúdo')
    date_created = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.title}'
