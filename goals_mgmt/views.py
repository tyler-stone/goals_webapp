from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from models import Goal, GoalForm

@login_required(login_url='/login/')
def home(request):
	user = request.user.get_full_name
	user_goals = Goal.objects.filter(owner__username=request.user.username)

	inbox_goals = user_goals.filter(unread=True)
	num_inbox_goals = len(inbox_goals)
	
	overdue_goals = user_goals.filter(flag__title="Overdue", unread=False)
	num_overdue_goals = len(overdue_goals)

	today_goals = user_goals.filter(flag__title="Due Today", unread=False)
	num_today_goals = len(today_goals)

	all_goals = user_goals.filter(flag__title="None", unread=False)
	num_all_goals = len(all_goals)

	complete_goals = user_goals.filter(flag__title="Complete", unread=False)
	num_complete_goals = len(complete_goals)

	total_goals = num_complete_goals + num_all_goals + num_inbox_goals + num_overdue_goals + num_today_goals
	return render(request, 'home.html', {
		'user':user, 
		'total_goals':total_goals, 
		'inbox_goals':inbox_goals,
		'overdue_goals':overdue_goals, 
		'today_goals':today_goals,
		'all_goals':all_goals,
		'complete_goals':complete_goals,
		})

@login_required(login_url="/login/")
def new(request):
	user = request.user.get_full_name

	if request.method == 'POST':
		form = GoalForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/goals/home')
	else:
		form = GoalForm()

	return render(request, 'new.html', {
		'user':user,
		'form':form,
		})

def redirect(request):
	return HttpResponseRedirect('/goals/home')