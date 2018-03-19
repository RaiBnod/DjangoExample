from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(_('Question ho bhai'), max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def when_published(self):
        return self.pub_date

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

