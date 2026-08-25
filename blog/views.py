from django.shortcuts import get_object_or_404, render, redirect

from blog.forms import CommentForm, PostEditForm, CreatePostForm
from blog.models import Post, Comment, Category


def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category)
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()

            return redirect('blog_detail', slug=slug)

    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)

def create_blog(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('blog_index')
    else:
        form = CreatePostForm()

    context = {
        'form': form,
    }
    return render(request, 'blog/create.html', context)

def blog_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_index")
    else:
        form = PostEditForm(instance=post)
    context = {
        "form": form,
    }
    return render(request, 'blog/edit.html', context)