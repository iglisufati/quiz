from rest_framework import serializers
from questions.serializers import QuestionSerializer


class ResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    questions = QuestionSerializer(many=True)
    difficulty_level = serializers.IntegerField(default=0)
    points = serializers.IntegerField(default=0)
    timer = serializers.IntegerField(default=0)