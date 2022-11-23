from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    content = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question: {self.question.content}, answer: {self.content}"
