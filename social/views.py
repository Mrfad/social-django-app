from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            newform = form.save(commit=False)
            newform.author = request.user
            newform.save()
        
        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'social/post_list.html', context)
