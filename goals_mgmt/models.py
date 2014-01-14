from __future__ import division
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from templatetags.tags import space_to_dash

GOAL_STATUS_CHOICES = (
	('None', 'None'),
	('Important', 'Important'),
	('Awaiting Reply', 'Awaiting Reply'),
	('Working On It', 'Working On It'),
	('Almost Done', 'Almost Done'),
	('Talk to Board', 'Talk to Board'),
	('Discuss at Meeting', 'Discuss at Meeting'),
)

SUBGOAL_STATUS_CHOICES = (
	('None', 'None'),
	('Important', 'Important'),
	('Complete', 'Complete'),
)

class Goal(models.Model):
	title = models.CharField(max_length=255)
	goal_type = models.ForeignKey('GoalType')
	unread = models.BooleanField()
	notes = models.TextField()
	status = models.CharField(max_length=64, choices=GOAL_STATUS_CHOICES)
	flag = models.ForeignKey('Flag')
	owner = models.ForeignKey(User)
	date_created = models.DateField(auto_now_add=True, editable=False)
	last_update = models.DateField(auto_now=True, editable=False)
	date_due = models.DateField()

	def __unicode__(self):
		return self.title

	def color_class(self):
		if self.unread:
			return "inbox"
		else:
			return space_to_dash(self.flag.title).lower()

	def completeness(self):
		total = 0
		totalDone = 0
		for x in self.subgoal_set.all():
			total += 1;
			if x.status == "Complete":
				totalDone += 1;
		if total > 0:
			return round((totalDone / total) * 100, 1)
		else:
			return 0

	class Meta:
		ordering = ['-date_due', '-last_update']

class SubGoal(models.Model):
	title = models.CharField(max_length=255)
	status = models.CharField(max_length=64, choices=SUBGOAL_STATUS_CHOICES)
	owner = models.ForeignKey('Goal')
	
	def __unicode__(self):
		return self.title

class Flag(models.Model):
	title = models.CharField(max_length=64)
	icon = models.ImageField(upload_to='icons')

	def __unicode__(self):
		return self.title

class GoalType(models.Model):
	title = models.CharField(max_length=64)

	def __unicode__(self):
		return self.title

class GoalForm(ModelForm):
	class Meta:
		model=Goal
		fields = ['title', 'notes', 'status', 'owner', 'date_due']
