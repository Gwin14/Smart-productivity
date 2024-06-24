from django.contrib import admin
from notesApp import models


# Register your models here.

@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created')
    ordering = 'id',
    search_fields = ('title', 'date_created', 'tags__name')
