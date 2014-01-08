from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
	title = models.CharField(max_length=255)
	goal_type = models.BooleanField()
	notes = models.TextField()
	flag = models.CharField(max_length=64)
	owner = models.ForeignKey(User)
	date_created = models.DateTimeField(auto_now_add=True, editable=False)
	last_update = models.DateTimeField(auto_now=True, editable=False)
	date_due = models.DateTimeField()

	def __unicode__(self):
		return self.title

class SubGoal(models.Model):
	title = models.CharField(max_length=255)
	flag = models.CharField(max_length=64)
	owner = models.ForeignKey('Goal')
	
	def __unicode__(self):
		return self.title