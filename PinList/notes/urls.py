from django.urls import path
from .views import BulkNotesView, EditNoteView

urlpatterns = [
    path('list/', BulkNotesView.as_view(), name='note_bulk'),
    path('list/<int:pk>/', EditNoteView.as_view(), name='note_edit')
]