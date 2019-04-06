from django.shortcuts import render
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
        photo_main = request.POST['profile']
        photo_1 = request.POST['profile1']
        photo_2 = request.POST['profile2']
        description = request.POST['description']

        item_report = Post(title=title,item_type=item_type,tag=tag,location=location,city=city,state=state,photo_main=photo_main,photo_1=photo_1,photo_2=photo_2,description=description)
        item_report.save()
    return render(request,'post/report.html')


