from django.shortcuts import render, get_object_or_404
from .models import PostProduct, Category

def blog(req):
    posts = PostProduct.objects.all()
    return render(req, 'venta/blog.html', {"posts": posts})

def category(req, category_id):
    ctg = Category.objects.get(id = category_id)
    posts = PostProduct.objects.filter(categories = ctg)
    #ctg = get_object_or_404(Category,id = category_id)
    return render(req, 'venta/category.html', {"ctg": ctg})