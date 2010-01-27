from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    term = models.CharField(max_length=200)
    createdTime = models.DateTimeField('first date submitted')
    createdBy = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.term
        
class Defination(models.Model):
    meaning = models.CharField(max_length=1000)
    sentence = models.CharField(max_length=1000)
    ofWord = models.ForeignKey(Word)
    addedTime = models.DateTimeField('date submitted')
    addedBy = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.meaning