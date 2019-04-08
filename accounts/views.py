from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import UserInfoForm,ExtendUserCreationForm
def register(request):
    if request.method == 'POST':

        form = ExtendUserCreationForm(request.POST)
        user_info = UserInfoForm(request.POST,request.FILES)
        if form.is_valid() and user_info.is_valid():
            user = form.save()
            user_detail = user_info.save(commit=False)
            user_detail.user = user
            user_detail.save()
            return redirect('login')
    else:
        form = ExtendUserCreationForm()
        user_info = UserInfoForm()
    context = {
        'form':form,
        'user_info':user_info
    }
    return render(request,'accounts/register.html',context)

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')