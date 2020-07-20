from django.urls import path

from . import views

urlpatterns = [
    path('download', views.download, name='download'),
    path('caption_to_srt/', views.caption_to_srt, name='caption_to_srt'),
]
