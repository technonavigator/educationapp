from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    TYPES = (
        ('lecture', 'Лекция'),
        ('video', 'Видео'),
        ('document', 'Документ'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    lesson_type = models.CharField(max_length=10, choices=TYPES)
    file = models.FileField(upload_to='materials/', blank=True, null=True)
    filepath = models.CharField(max_length=100)
