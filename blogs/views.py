from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from blogs.models import Blog, Category


# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context = {
        'posts' : posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)