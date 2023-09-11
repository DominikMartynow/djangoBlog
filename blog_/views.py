from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from .models import Post, Comment, Like, User
from .forms import CommentForm

# Create your views here.
def index(request):
    """Wyświetla stronę główną"""
    posts = Post.objects.all().values().order_by('-date_added')
    context = {'posts': posts}

    return render(request, 'blog_/index.html', context)

@require_http_methods(['POST', 'GET'])
@login_required
def post(request, post_id):
    """Wyświetla cały post z komentarzami"""
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.order_by('-date_added')
    form = CommentForm(data=request.POST)
    likes = list(Like.objects.filter(post = post_id).order_by('-date_added'))
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.owner = request.user
        new_comment.post = post
        new_comment.save()
        print(new_comment.owner)
        return redirect('blog_:post', post_id=post_id)
        
    likesCount = len(list(Like.objects.filter(post = post_id)))

    if len(list(Like.objects.filter(post = post_id).filter(owner = request.user))) == 0:
        if_clicked = False
    else:
        if_clicked = True

    context = {'post': post, 'comments': comments, 'form': form, 'likesCount': likesCount, 'if_clicked': if_clicked, 'likes': likes,}

    return render(request, 'blog_/post.html', context)

@require_http_methods(['POST', 'GET'])
@login_required
def like(request, post_id):
    """Like"""
    post = Post.objects.get(id=post_id)

    if len(list(Like.objects.filter(post = post_id).filter(owner = request.user))) == 0:
        new_like = Like(post=post)
        new_like.owner = request.user
        new_like.save()
    else: 
        Like.objects.filter(post = post_id).filter(owner = request.user).delete()

    return redirect('blog_:post', post_id=post_id)

@login_required
def usersList(request):
    users = get_user_model().objects.all().values()

    context = {'users': users}

    return render(request, 'blog_/users_list.html', context)

@login_required
def userProfile(request, user_id):
    user_values = get_user_model().objects.all().values().filter(id=user_id)
    user_values = user_values[0]

    posts_liked = Like.objects.all().filter(owner=user_id).order_by('-date_added')
    posts_commented = Comment.objects.all().filter(owner=user_id).order_by('-date_added')
    context = {'user_values': user_values, 'posts_liked': posts_liked, 'posts_commented': posts_commented}

    return render(request, 'blog_/userProfile.html', context)

def deleteComment(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.get(id=comment_id)

    if comment.owner == request.user:
        comment = comment.delete()
    else:
        print("e")

    return redirect('blog_:post', post_id=post_id)
