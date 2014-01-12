from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponseRedirect
from models import Goal, Flag

def update_flags(request):
	check_goals = Goal.objects.filter(~Q(status__title="Complete"), ~Q(status__title="Archived"))
	for x in check_goals:
		if x.date_due < timezone.now().date():
			x.flag = Flag.objects.get(title="Overdue")
		elif x.date_due == timezone.now().date():
			x.flag = Flag.objects.get(title="Due Today")
		else:
			x.flag = Flag.objects.get(title="None")
		x.save()
	return HttpResponseRedirect('/goals/home')