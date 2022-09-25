from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from base.models import ResponseModel
from .serializers import ResponseSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    response = ResponseModel.objects.all()
    serializer = ResponseSerializer(response, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postData(request):
    serializer = ResponseSerializer(data = request.data)
    if  serializer.is_valid():
        serializer.save()
    return Response(serializer.data)