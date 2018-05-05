from django.db import models
from django.utils import timezone

class Document(models.Model):
    name = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='assignments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
