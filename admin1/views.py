from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from admin1.models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
	return render(request, 'dashboard.html')

def login(request):
	return render(request, 'login.html')

def check_login(request):
	if request.method =="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/dashboard')
	else:
		return redirect('/login')

def logout(request):
	auth.logout(request)
	return redirect('/login')

@login_required(login_url='/login')
def dashboard(request):
	return render(request, 'dashboard.html')

@login_required(login_url='/login')
def profile(request):
	data1 = Profile.objects.filter(user=request.user) 
	return render(request, 'profile.html', { 'data1' : data1})

@login_required(login_url='/login')
def create_user(request):
	auth.logout(request)
	return render(request, 'create.html')

@login_required(login_url='/login')
def data_stored(request):
	user= User.objects.create_user(username=request.POST['username'], first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'])
	auth.login(request, user)
	info= Profile(user=request.user, address=request.POST['address'], phone_no=request.POST['phone_no'], dob=request.POST['dob'])
	info.save()
	return redirect('/dashboard')

@login_required(login_url='/login')
def edit_profile(request, id):
	edit_profile = Profile.objects.filter(id=id) 
	return render(request, 'profile.html', { 'edit_profile' : edit_profile})

@login_required(login_url='/login')
def data_updated(request,id):
	info= Profile(id=id, address=request.POST['address'], phone_no=request.POST['phone_no'], dob=request.POST['dob'])
	info.save()
	return redirect('/profile')
