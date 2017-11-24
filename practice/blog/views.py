from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def index(request, pageNumber = 0):
    pageNumber = int(pageNumber)
    startIndex = pageNumber * 10 + 1
    endIndex = (pageNumber + 1) * 10
    post_list = Post.objects.filter(id__range=(startIndex, endIndex))
    return render(request, 'blog/index.html', context = {'posts': post_list, 
                                                         'currentPage': pageNumber,
                                                         'prevPage': pageNumber - 1,
                                                         'nextPage': pageNumber + 1})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', context = {'post': post})