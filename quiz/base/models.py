from django.db import models

# Create your models here.

class AnswerModel(models.Model):
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answer'

    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)


    def get_answer(self):
        return self

class QuestionModel(models.Model):
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'question'

    question_text = models.CharField(max_length=200)
    answer = models.OneToOneField(AnswerModel, related_name='answer', on_delete=models.CASCADE, default="Some String")

    def get_question(self):
        return self


class ResponseModel(models.Model):
    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'
        db_table = 'response'

    questions = models.ForeignKey(QuestionModel, related_name='question', on_delete=models.CASCADE)
    difficulty_level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    timer = models.IntegerField(default=0)

    def get_response(self):
        return self
