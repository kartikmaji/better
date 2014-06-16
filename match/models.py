from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Match(models.Model):
    team1 = models.CharField(max_length=32)
    team2 = models.CharField(max_length=32)
    def __unicode__(self):
        return (self.team1+"_vs_"+ self.team2)
    date_time = models.DateTimeField("Match Date_time")
    
