from django.db import models


class HourEntry(models.Model):
    
    name = models.CharField(max_length=30)
    project = models.CharField(max_length=40)
    task = models.CharField(max_length=30)
    notes = models.TextField(max_length=4)
    pub_date = models.DateField('Date Worked')
    hours = models.CharField(max_length=10)
    cost = models.IntegerField(default=0)
    billable = models.BooleanField(default=False)
    billed = models.BooleanField(default=False)
    class Meta:
    	verbose_name_plural = "Hour Entries"
       
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
