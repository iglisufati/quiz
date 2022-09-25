from rest_framework import serializers
from base.models import QuestionModel,ResponseModel,AnswerModel

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = '__all__'



class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        fields = '__all__'