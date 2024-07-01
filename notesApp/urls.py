from django.urls import path
from notesApp import views

urlpatterns = [
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('auth/', views.auth_options, name='auth'),

    # NOTES CREATION AND UPDATING

    path('notes/create/', views.create_note, name='create_note'),
    path('notes/delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('notes/update/<int:note_id>/', views.update_note, name='update_note'),

    # USER AUTHENTICATION

    path('user/create/', views.register, name='register'),
    path('user/login/', views.user_login, name='login'),
    path('user/logout/', views.user_logout, name='logout'),
    path('user/update/', views.user_update, name='user_update'),

    # GOOGLE CHATBOT

    path('chatbot/', views.chatbot_view, name='chatbot'),
]
