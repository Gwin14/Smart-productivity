from django.apps import AppConfig


class NotesappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notesApp'

    def ready(self):
        import notesApp.signals
