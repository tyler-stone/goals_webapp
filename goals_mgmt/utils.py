from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponseRedirect
from models import Goal, Flag

def update_flags(request):
	check_goals = Goal.objects.filter(~Q(flag__title="Complete"))
	time_now = timezone.localtime(timezone.now()).date()
	for x in check_goals:
		if x.date_due == time_now:
			x.flag = Flag.objects.get(title="Due Today")
		elif x.date_due < time_now:
			x.flag = Flag.objects.get(title="Overdue")
		else:
			x.flag = Flag.objects.get(title="None")
		x.save()
	return HttpResponseRedirect('/goals/home')