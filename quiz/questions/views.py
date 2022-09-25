from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from  base.models import QuestionModel
from  questions.serializers import QuestionSerializer


class QuestionsLCView(APIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_class = RecipeFilterSerializer
#     ordering_fields = ['code', 'labour_cost', 'product']

    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def getQuestion(request):
        question = QuestionModel.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)