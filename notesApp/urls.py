from django.contrib import admin
from django.urls import path
from notesApp import views

urlpatterns = [
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('', views.index, name='index'),
]
