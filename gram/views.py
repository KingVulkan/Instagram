from django.http  import Http404
from django.shortcuts import render,redirect
from . models import Image ,Profile, Like, Follow, Comment
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . forms import ImageForm, CommentForm, ProfileUpdateForm,UpdateImageCaption 
import os
from django.template.defaulttags import register


# Create your views here.

@login_required(login_url='/accounts/login/')
def timeline(request):
    date = dt.date.today()
    current_user = request.user 
    followed_people= []
    images1 =[]
    following  = Follow.objects.filter(follower = current_user)
    is_following = Follow.objects.filter(follower = current_user).count()
    try:
        if is_following != 0:
            for folling_object in following:
                image_set = Profile.objects.filter(id = folling_object.user.id)
                for item in image_set:
                    followed_people.append(item)
            for followed_profile in followed_people:
                post = Image.objects.filter(user_key = followed_profile.user)
                for item in post:
                    images1.append(item)
                    images= list(reversed(images1))                                                                                                                                                                                                                                                                                                                                                                  
            return render(request, 'all-grams/timeline.html',{"date":date,"timeline_images":images})
    except:
        raise Http404
    return render(request, 'all-grams/first_time.html') 

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'name' in request.GET and request.GET["name"]: 
        search_name = request.GET.get("name")
        found_users = Profile.find_profile(search_name)
        message =f"{search_name}" 

        return render(request,'all-grams/search_results.html',{"message":message,"found_users":found_users})
    else:
        message = "Please enter a valid username"
    return render(request,'all-grams/search_results.html',{"message":message})


@login_required(login_url='/accounts/login/')
def single_user(request,id):
    try:
        user = Profile.objects.get(id=id)
    except:
        raise Http404()
    return render(request,'all-grams/single.html',{"user":user})

@login_required(login_url='/accounts/login/')
def single_image(request,image_id): 
    try:
        image = Image.objects.get(id= image_id)
    except:
        raise Http404()
    return render(request, 'all-grams/single_image.html',{"image":image})


@login_required(login_url='/accounts/login/')
def post(request):
    '''
    View function that displays a forms that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImageForm(request.POST ,request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.user_key = current_user
            image.likes +=0
            image.save() 

            return redirect( timeline)
    else:
        form = ImageForm() 
    return render(request, 'all-grams/post.html',{"form" : form}) 
