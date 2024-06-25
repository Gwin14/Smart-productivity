from django.urls import path
from notesApp import views

urlpatterns = [
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    path('notes/create/', views.create_note, name='create_note'),
]
