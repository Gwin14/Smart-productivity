import markdown

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from notesApp.forms import NoteForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from notesApp.models import Note
from django.db.models import Q

from django.http import JsonResponse
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Create your views here.


@login_required(login_url='auth')
def index(request):

    notes = Note.objects.filter(owner=request.user).order_by('-date_created')

    context = {
        'notes': notes,
        'title': 'Notes App',
    }

    return render(request, 'notesApp/index.html', context=context)


def auth_options(request):
    return render(request, 'notesApp/auth_options.html')


@login_required(login_url='auth')
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    notes = Note.objects.filter(owner=request.user).order_by('-date_created')

    note.content_html = markdown.markdown(note.content)

    context = {
        'notes': notes,
        'note': note,
    }

    return render(request,
                  'notesApp/note_detail.html',
                  context=context)


@login_required(login_url='auth')
def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('index')

    notes = Note.objects.filter(
        Q(owner=request.user) & (
            Q(title__icontains=search_value) |
            Q(content__icontains=search_value) |
            Q(date_created__icontains=search_value) |
            Q(tags__name__icontains=search_value)
        )
    ).distinct().order_by('-date_created')

    context = {'notes': notes, 'title': 'Notes App'}
    return render(request, 'notesApp/index.html', context=context)


@login_required(login_url='auth')
def create_note(request):
    notes = Note.objects.all().order_by('-date_created')

    if request.method == 'POST':

        form = NoteForm(request.POST, request.FILES)

        context = {
            'notes': notes,
            'form': form,
        }

        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            form.save_m2m()
            return redirect('note_detail', note_id=note.pk)

        return render(request, 'notesApp/create_note.html', context=context)

    context = {
        'notes': notes,
        'form': NoteForm()
    }

    return render(request, 'notesApp/create_note.html', context=context)


@login_required(login_url='auth')
def delete_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect('index')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'notesApp/register.html', context=context)


def user_login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('index')

    context = {
        'form': form,
        'title': 'Login'
    }

    return render(request, 'notesApp/login.html', context=context)


def user_logout(request):
    auth.logout(request)
    return redirect('auth')


# IA DO GOOGLE CHATBOT
load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


@login_required(login_url='auth')
def chatbot_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')

        if question.strip() == '':
            return JsonResponse({'error': 'Empty question'}, status=400)

        response = chat.send_message(question)
        html_response = markdown.markdown(response.text)
        return JsonResponse({'response': html_response})

    return render(request, 'notesApp/chatbot.html')
