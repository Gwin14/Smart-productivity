from django.urls import path
from notesApp import views

urlpatterns = [
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('auth/', views.auth_options, name='auth'),

    # NOTES CREATION AND UPDATING

    path('notes/create/', views.create_note, name='create_note'),

    # USER AUTHENTICATION

    path('user/create/', views.register, name='register'),
    path('user/login/', views.user_login, name='login'),
    path('user/logout/', views.user_logout, name='logout'),

    # IA DO GOOGLE CHATBOT

    path('chatbot/', views.chatbot_view, name='chatbot'),
]
