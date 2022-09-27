from django.urls import path

from .views import ResponseLCView

urlpatterns = [
    path('response/', ResponseLCView.getResponse, name='response'),
    ]