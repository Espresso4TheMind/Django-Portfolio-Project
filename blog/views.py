from django.shortcuts import render, redirect
from blog.models import Post, Comment
from blog.forms import CommentForm


def blog_index(request):
    page_title = 'Personal Blog'
    posts = Post.objects.exclude(display='Private').order_by('-created_on')
    context = {
        'posts': posts,
        'page_title': page_title,
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
            return redirect('blog_detail', pk=pk)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'page_title': post.title
    }
    return render(request, 'blog_detail.html', context)


def blog_tags(request, tags):
    posts = Post.objects.filter(tags__name__contains=tags).exclude(display='Private').order_by('-created_on')
    context = {
        'tags': tags,
        'posts': posts,
        'page_title': tags,
    }
    return render(request, 'blog_index.html', context)
