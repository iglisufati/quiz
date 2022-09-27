from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from  base.models import ResponseModel
from  response.serializers import ResponseSerializer


class ResponseLCView(APIView):
    queryset = ResponseModel.objects.all()
    serializer_class = ResponseSerializer

    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def getResponse(request):
        response = ResponseModel.objects.all()
        serializer = ResponseSerializer(response, many=True)
        return Response(serializer.data)