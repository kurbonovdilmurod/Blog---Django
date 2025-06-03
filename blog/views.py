from django.shortcuts import get_object_or_404, render, redirect

from blog.forms import CommentForm
from blog.models import Post


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)



def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', slug=slug)

    else:
        form = CommentForm()


    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)
