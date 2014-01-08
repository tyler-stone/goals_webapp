from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_user(request):
	state = "Please log in below..."
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "you've logged in"
			else:
				state = "your account is not active"
		else:
			state = "username/password wrong"

	return render_to_response('auth.html', {'state':state, 'username':username})