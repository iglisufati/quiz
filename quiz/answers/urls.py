from django.urls import path


from .views import AnswersLCView

urlpatterns = [
    path('answers/', AnswersLCView.getAnswers, name='answers'),
    ]