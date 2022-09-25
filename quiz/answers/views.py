from django.shortcuts import render

# Create your views here.

# Create your views here.
from rest_framework.views import APIView

from  base.models import AnswerModel
from  answers.serializers import AnswerSerializer


class AnswersLCView(APIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer