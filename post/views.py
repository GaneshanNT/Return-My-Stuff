from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages, auth
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    post_detail = Post.objects.order_by('-date').filter(is_published = True)
    content = {
        'post_detail': post_detail
    }
    return render(request,'post/index.html',content)


def report(request):
    if request.method == 'POST':
        report_form = PostForm(request.POST,request.FILES)

        if report_form.is_valid():
            instance = report_form.save(commit=False)
            instance.reporter = request.user
            instance.save()
            messages.success(request,'Your report has been successfully created!')
            return redirect('home')
    else:
        report_form = PostForm()
    context = {
        'report_form':report_form
    }
    return render(request, 'post/report.html',context)

def reportdetail(request,report_id):
    post_detail = get_object_or_404(Post,pk=report_id)
    context = {
        'post_detail': post_detail
    }
    return render (request,'post/detail.html',context)
