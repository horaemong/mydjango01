from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404

from app.models import Post


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(
        request,
        "app/index.html",
        {
            "post_list": qs,
        },
    )


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # qs = Post.objects.get(pk=pk)
    post_list = get_object_or_404(Post, pk=pk)
    return render(
        request,
        "app/post_detail.html",
        {
            "post": post_list,
        },
    )
