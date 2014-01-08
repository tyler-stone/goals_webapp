from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
	title = models.CharField(max_length=255)
	goal_type = models.ForeignKey('GoalType')
	unread = models.BooleanField()
	notes = models.TextField()
	status = models.ForeignKey('Status')
	flag = models.ForeignKey('Flag')
	owner = models.ForeignKey(User)
	date_created = models.DateField(auto_now_add=True, editable=False)
	last_update = models.DateField(auto_now=True, editable=False)
	date_due = models.DateField()

	def __unicode__(self):
		return self.title

class SubGoal(models.Model):
	title = models.CharField(max_length=255)
	status = models.ForeignKey('Status')
	owner = models.ForeignKey('Goal')
	
	def __unicode__(self):
		return self.title

class Flag(models.Model):
	title = models.CharField(max_length=64)
	color = models.CharField(max_length=8)
	icon = models.ImageField(upload_to='icons')

	def __unicode__(self):
		return self.title

class Status(models.Model):
	title = models.CharField(max_length=64)

	def __unicode__(self):
		return self.title

class GoalType(models.Model):
	title = models.CharField(max_length=64)

	def __unicode__(self):
		return self.title