from django.shortcuts import render,redirect
from .models import Post, Profile,Hood, Comment, Business
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import UpdateProfileForm,NewPostForm,CommentForm,NewBusinessForm,NewHoodForm
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
@login_required(login_url = '/accounts/login/')
def home(request):

    all_posts = Post.all_posts()
    hoods = Hood.objects.all()
    businesses = Business.objects.all()
    return render(request,'home.html',{'all_posts':all_posts,'hoods':hoods,'businesses':businesses})

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
    

# @login_required(login_url = '/accounts/login/')
# def newbiz(request):
#     if request.method=='POST':
#         form = NewBusinessForm(request.POST,request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()

#             return redirect('home')

#     else:
#         form = NewPostForm()
#     return render(request,'newbiz.html',{'form':form})


# @login_required(login_url = '/accounts/login/')
# def newhood(request):
#     if request.method=='POST':
#         form = NewHoodForm(request.POST,request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()

#             return redirect('home')

#     else:
#         form = NewPostForm()
#     return render(request,'newhood.html',{'form':form})

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
def search_results(request):

    if 'post' in request.GET and request.GET['post']:
        search_term = request.GET.get('post')
        searched_posts = Post.search_post(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{'message':message,'post':searched_posts})

    else:
        message = 'You havnt entered anything'
        return render(request,'search.html',{'message':message})



@login_required(login_url = '/accounts/login/')
def post(request,id):  
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post_id = id)
    return render(request,'post.html',{'post':post,'id':id,'comments':comments})


def logoutUser(request):
 logout(request)
 return redirect('home')



