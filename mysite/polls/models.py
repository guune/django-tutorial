import datetime

from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField("data published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> bool:
        return self.pubdata >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
