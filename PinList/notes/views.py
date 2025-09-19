from rest_framework.views import APIView
from .models import NotesModel
from .serializers import NoteSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class BulkNotesView(APIView):
    def get(self, request):
        try:
            all_notes = NotesModel.objects.all()
            serializer = NoteSerializer(all_notes, many=True)
            data = serializer.data
            return Response(data={"message": "Notes Retreived successfully.", "data":data}, status=status.HTTP_200_OK)
        except:
            return Response(data={"message": "Some Error Occurred."}, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        try:
            data = request.data
            serializer = NoteSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise Exception(serializer.errors)
            return Response(data={"message": "Notes Added successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))
            return Response(data={"message": "Some Error Occurred."}, status=status.HTTP_400_BAD_REQUEST)

class EditNoteView(APIView):
    def get(self, request, pk):
        try:
            note = NotesModel.objects.filter(id=pk).first()
            serializer = NoteSerializer(note)
            data = serializer.data
            return Response(data={"message": "Note Retreived successfully.", "data":data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response(data={"message": "Some Error Occurred."}, status=status.HTTP_400_BAD_REQUEST) 
    def put(self, request, pk):
        try:
            data = request.data
            note = NotesModel.objects.filter(id=pk).first()
            serializer = NoteSerializer(instance=note, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={"message": "Note updated successfully."}, status=status.HTTP_200_OK)
        except:
            return Response(data={"message": "Some Error Occurred."}, status=status.HTTP_400_BAD_REQUEST) 
    def delete(self, request, pk):
        try:
            note = get_object_or_404(NotesModel, pk=pk)
            note.delete()
            return Response(data={"message": "Notes Deleted successfully."}, status=status.HTTP_200_OK)
        except:
            return Response(data={"message": "Some Error Occurred."}, status=status.HTTP_400_BAD_REQUEST) 

