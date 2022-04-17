from django.shortcuts import render,redirect
from .models import Post, Profile,Category, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import UpdateProfileForm,NewPostForm,CommentForm
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def home(request):

    all_posts = Post.all_posts()
    return render(request,'home.html',{'all_posts':all_posts})

@login_required(login_url = '/accounts/login/')
def profile(request):
    user = request.user
    all_posts = Post.objects.filter(user = user)
    
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    else:
        form = UpdateProfileForm(request.POST,request.FILES)
    
    return render(request,'profile.html',{'all_posts':all_posts, 'form':form})


@login_required(login_url = '/accounts/login/')
def new_post(request):
    if request.method=='POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('home')

    else:
        form = NewPostForm()
    return render(request,'new_post.html',{'form':form})

@login_required(login_url = '/accounts/login/')
def comment(request,id):
    id = id
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            post = Post.objects.get(id = id)
            comment.post_id = post
            comment.save()
            return redirect('post',id)

        else:
            post_id = id
            messages.info(request,'fill all fields')
            return redirect('post',id)

    else:
        id = id
        form = CommentForm()
        return render(request,'comment.html',{'form':form,'id':id})

@login_required(login_url = '/accounts/login/')
def post(request,id):  

    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post_id = id)
    categories = Category.objects.filter(post_id = id)
    designrating = []
    usabilityrating = []
    contentrating= []
    if categories:
        for rating in categories:
            designrating.append(rating.design)
            usabilityrating.append(rating.usability)
            contentrating.append(rating.content)

        total = len(designrating)*10
        design = round(sum(designrating)/total*100,1)
        usability = round(sum(usabilityrating)/total*100,1)
        content = round(sum(contentrating)/total*100,1)
        return render(request,'post.html',{'post':post,'comments':comments,'design':design,'usability':usability,'content':content})


@login_required(login_url = '/accounts/login/')
def rate(request,id):
    id=id
    if request.method =='POST':
        categories = Category.objects.filter(id = id)
        for rating in categories:
            if rating.user == request.user:
                messages.info(request,'You can only rate once')
                return redirect('post',id)
        design = request.POST.get('design')
        usability = request.POST.get('usability')
        content = request.POST.get('content')

        if design and usability and content:
            post = Post.objects.get(id = id)
            rating = Category(design = design,usability = usability,content = content,post_id = post,user = request.user)
            rating.save()
            return redirect('post',id)

        else:
            messages.info(request,'enter required fields')
            return redirect('post',id)


    else:
        messages.info(request,'enter required fields')
        return redirect(post,id)

def logoutUser(request):
 logout(request)
 return redirect('home')



