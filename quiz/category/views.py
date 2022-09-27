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

from  base.models import CategoryModel
from  category.serializers import CategorySerializer


class CategoryLCView(APIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def getCategories(request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)