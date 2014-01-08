from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf

def login_user(request):
	state = "Please log in below..."
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		next = request.POST.get('next')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				state = "your account is not active"
		else:
			state = "username/password wrong"

	return render(request, 'auth.html', {'state':state, 'username':username})