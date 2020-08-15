from django.shortcuts import render
from django.utils import timezone
from .models import Post, CV


def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by(
        "publish_date"
    )
    return render(request, "blog/post_list.html", {"posts": posts})


def post(request, post_id):
    post = Post.objects.get(post_id=post_id)
    return render(request, "blog/post.html", {"post": post})


def latest_cv(request):
    cv = CV.objects.all().order_by("last_updated")[0]
    return render(request, "blog/cv.html", {"cv": cv})


def cv(request, revision_date):
    cv = CV.objects.get(last_updated=revision_date)
    return render(request, "blog/cv.html", {"cv": cv})
