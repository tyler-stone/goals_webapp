from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from models import Goal

@login_required(login_url='/login/')
def home(request):
	user = request.user.get_full_name
	user_goals = Goal.objects.filter(owner__username=request.user.username)
	
	inbox_goals = user_goals.filter(unread='true')
	num_inbox_goals = len(inbox_goals)
	
	overdue_goals = user_goals.filter(flag__title="Overdue")
	num_overdue_goals = len(overdue_goals)

	today_goals = user_goals.filter(flag__title="Due Today")
	num_today_goals = len(today_goals)

	return render(request, 'home.html', {'user':user, 'inbox_goals':inbox_goals, 'num_inbox_goals':num_inbox_goals, 'overdue_goals':overdue_goals, 'num_overdue_goals':num_overdue_goals, 'today_goals':today_goals, 'num_today_goals':num_today_goals})

def redirect(request):
	return HttpResponseRedirect('/goals/')