from django.db import models

class NotesModel(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

