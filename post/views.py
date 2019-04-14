from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from django.contrib import messages, auth
from .models import Post
from .forms import PostForm,RequestForm
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    post_detail = Post.objects.order_by('-date').filter(is_published = True)

    paginator = Paginator(post_detail,3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    pagination= paginator.get_page(page)


    content = {
        'post_detail':pagination, 
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
    
def requestitem(request):
    if request.method =='POST':
        request_form = RequestForm(request.POST,request.FILES)

        if request_form.is_valid():
            instance = request_form.save(commit=False)
            instance.requester = request.user
            instance.save()
<<<<<<< HEAD
            return HttpResponse("<h3> Request form submitted successfully. <br> Reporter get back to you soon <br> Hope for the BEST </h3>")
=======
            return HttpResponseRedirect("<h3> Request form submitted successfully. <br> Reporter get back to you soon <br> Hope for the BEST </h3>")
>>>>>>> a4e69c74ad142eb9f7318b794860d863478518f5
    else:
        request_form=RequestForm()
    context = {
        'request_form':request_form
    }
    return render(request,'post/request.html',context)



