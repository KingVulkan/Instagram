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