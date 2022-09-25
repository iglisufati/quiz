from rest_framework import serializers

class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    answer_text = serializers.CharField(max_length=200)
    is_correct = serializers.BooleanField(default=False)