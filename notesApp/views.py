from django.shortcuts import get_object_or_404, redirect, render
from notesApp.forms import NoteForm
from notesApp.models import Note
from django.db.models import Q

# Create your views here.


def index(request):

    notes = Note.objects.all().order_by('-date_created')

    context = {
        'notes': notes,
        'title': 'Notes App',
    }

    return render(request, 'notesApp/index.html', context=context)


def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    notes = Note.objects.all().order_by('-date_created')

    context = {
        'notes': notes,
        'note': note,
    }

    return render(request,
                  'notesApp/note_detail.html',
                  context=context)


def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('index')

    notes = Note.objects.filter(
        Q(title__icontains=search_value) |
        Q(content__icontains=search_value) |
        Q(date_created__icontains=search_value) |
        Q(tags__name__icontains=search_value)
    ).order_by('-date_created')

    context = {'notes': notes, 'title': 'Notes App'}
    return render(request, 'notesApp/index.html', context=context)


def create_note(request):

    notes = Note.objects.all().order_by('-date_created')

    if request.method == 'POST':

        form = NoteForm(request.POST)

        context = {
            'notes': notes,
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'notesApp/create_note.html', context=context)

    context = {
        'notes': notes,
        'form': NoteForm()
    }

    return render(request, 'notesApp/create_note.html', context=context)
