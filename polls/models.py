import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    ques_text = models.CharField('Question Text', max_length=200)
    pub_date = models.DateTimeField('Publication Date')

    def __str__(self):
        return self.ques_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
