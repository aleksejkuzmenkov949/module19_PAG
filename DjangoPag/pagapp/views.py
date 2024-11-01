from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.objects.all().order_by('-created_at')

    # Пагинация: 3 поста на странице
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'page_posts': page_posts, 'paginator': paginator})