from django.db import models

class Member(models.Model):
	name = models.CharField(max_length=64)
	position = models.CharField(max_length=128)
	password = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name

class Goal(models.Model):
	title = models.CharField(max_length=255)
	goal_type = models.BooleanField()
	notes = models.TextField()
	flag = models.CharField(max_length=64)
	owner = models.ForeignKey('Member')
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