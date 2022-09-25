from django.urls import path

from .views import QuestionsLCView

urlpatterns = [
    path('questions/', QuestionsLCView.getQuestion, name='questions'),
    ]