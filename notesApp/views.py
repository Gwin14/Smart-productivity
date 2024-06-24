from django.shortcuts import get_object_or_404, render
from notesApp.models import Note

# Create your views here.


def index(request):

    notes = Note.objects.all()

    context = {
        'notes': notes,
        'title': 'Notes App',
    }

    return render(request, 'notesApp/index.html', context=context)


def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    notes = Note.objects.all()

    context = {
        'notes': notes,
        'note': note,
    }

    return render(request,
                  'notesApp/note_detail.html',
                  context=context)
