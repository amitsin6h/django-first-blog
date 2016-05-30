from django.shortcuts import render
from django.utils import timezone
from .models import Post, Tweet
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TweetForm
# Create your views here.
def post_list(request):
	posts = Post.objects.all().order_by('-published_date')
	return render(request, 'post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post':post})


def tweet(request):
	form = TweetForm()
	if request.method == 'POST':
		form = TweetForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return HttpResponseRedirect('/blog')
		else:
			form = TweetForm()
	return render(request, 'index.html', {'form':form})


def tweet_list(request):
	tweet = Tweet.objects.all()
	return render(request, 'tweet_list.html', {'tweet':tweet})