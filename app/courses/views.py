from django.shortcuts import render
from .models import Lesson
import mimetypes

# Create your views here.
def download_file(request, filepath):
    # fill these variables with real values
    filename = 'downloaded_file_name.extension'

    fl = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def text_lect(request):
#    text_lections = Lessons.objects.filter(lesson_type=('document', 'Документ'))
    return render(request, 'courses/text_lections.html')

def pres_lect(request):
#    pres_lections = Lessons.objects.filter(lesson_type=('lecture', 'Лекция'))
    return render(request, 'courses/pres_lections.html')

def video_lect(request):
#    video_lections = Lessons.objects.filter(lesson_type=('video', 'Видео'))
    return render(request, 'courses/video_lect.html')
