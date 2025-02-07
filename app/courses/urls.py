from django.urls import path
from . import views


urlpatterns = [
    path('txtlect/', views.text_lect, name='textlect'),
    path('preslect/', views.pres_lect, name='preslect'),
    path('videolect/', views.video_lect, name='videolect'),
]
