from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.CharField(max_length=1000)
    example = models.CharField(max_length=1000)
    addedTime = models.DateTimeField('first date submitted')
    addedBy = models.ForeignKey(User)
    voteUp = models.IntegerField()
    voteDown = models.IntegerField()
    
    def __unicode__(self):
        return self.term