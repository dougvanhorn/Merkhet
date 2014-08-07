from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=60)
    def __unicode__(self):  
        return self.name
    class Meta:
	verbose_name_plural = "Projects"

class Task(models.Model):
    name = models.CharField(max_length=60)
    def __unicode__(self):  
        return self.name
    class Meta:
	verbose_name_plural = "Tasks"

class HourEntry(models.Model):
    
    name = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    task = models.ForeignKey(Task)
    notes = models.TextField(max_length=4)
    pub_date = models.DateField('Date Worked')
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.IntegerField(default=0)
    billable = models.BooleanField(default=False)
    billed = models.BooleanField(default=False)
    class Meta:
    	verbose_name_plural = "Hour Entries"
       



