from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from models import Goal

@login_required(login_url='/login/')
def home(request):
	user = request.user.get_full_name
	user_goals = Goal.objects.filter(owner__username=request.user.username)
	inbox_goals = user_goals.filter(unread='true')
	overdue_goals = user_goals.filter(flag__title="Overdue")
	today_goals = user_goals.filter(flag__title="Due Today")
	return render(request, 'home.html', {'user':user, 'inbox_goals':inbox_goals, 'overdue_goals':overdue_goals, 'today_goals':today_goals})

def redirect(request):
	return HttpResponseRedirect('/goals/')