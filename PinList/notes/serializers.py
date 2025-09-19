from rest_framework import serializers
from .models import NotesModel

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        fields = '__all__'