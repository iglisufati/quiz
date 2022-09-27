from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Create your views here.

# Create your views here.
from rest_framework.views import APIView

from  base.models import AnswerModel
from  answers.serializers import AnswerSerializer


class AnswersLCView(APIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer

    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def getAnswers(request):
        answers = AnswerModel.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)