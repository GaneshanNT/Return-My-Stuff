from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import *


# Create your views here.

def home(request):
    return render(request,'post/index.html')

def report(request):
    if request.method == 'POST':
        title = request.POST['title']
        item_type = request.POST['itemtype']
        tag =  request.POST['tag']
        location = request.POST['location']
        city = request.POST['city']
        state = request.POST['state']
        photo_main = request.FILES['profile']
        photo_1 = request.FILES['profile']
        photo_2 = request.FILES['profile']
        description = request.POST['description']

        if request.user.is_authenticated:
            reporter_id = request.user.id
            item_report = Post(title=title,item_type=item_type,tag=tag,location=location,city=city,state=state,photo_main=photo_main,photo_1=photo_1,photo_2=photo_2,description=description)
            item_report.save()
            messages.success(request, 'You are now registered and can log in')
    return render(request,'post/report.html')


