from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Tweet

from .forms import NewUserForm

import cloudinary


def index(request):
    print('Index function')
    userpost = Tweet.objects.filter(parent_tweet_id=None).order_by('-id')[:19]
    print('fetch userpost')
    for post in userpost:
        print('for userpost')
        post.replycount = Tweet.objects.filter(parent_tweet_id=post.id).count()
        print(post.replycount)
        # print(post.image == '')

    # print(userpost)
    content = {
        'post': userpost,
    }
    return render(request, 'index.html', content)


def posttweet(request):
    # context= {}
    # print("Started posttweet")
    # creating an object and assigning it with the instance
    form = NewUserForm()
    # print(form)
    # print("created form")
    if request.method == 'POST':
        print('printing post')
        print(request.POST)
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # print(form.save())
            return redirect(reverse('index'))
        else:
            print('ERROR FORM INVALID')
    # print("post completed")
    return render(request, 'posttweet.html', {'form': form})


def tweetdetail(request, id):
    atweet = Tweet.objects.get(id=id)
    replies = Tweet.objects.filter(parent_tweet_id=id)
    countreplies = replies.count()
    # print("Counting replies ")
    # print(countreplies)
    return render(request, 'tweetdetail.html', {'singletweet': atweet, 'replies': replies, 'countreplies': countreplies})


def reply(request, id):

    form = NewUserForm()
    # context = {'form': form}
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST['parent_tweet_id'] = id
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('tweetdetail', args=[id]))
        else:
            print(form.errors)
    return render(request, 'reply.html', {'form': form})

    # return render(request, 'reply.html')
    # return HttpResponse("You are in replying %s." %parent_tweet_id)
