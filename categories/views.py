from django.shortcuts import render
from categories.models import Category
from article.models import Article

# Create your views here.

# def CategoryView(request, slug_cate = None):
#     articles = Article.objects.all()
#     if slug_cate is not None:
#         category = Category.objects.get(slug = slug_cate)
#         articles = Article.objects.filter(category=category)
#     categories = Category.objects.all()
#     return render(request, "index.html", {"categories":categories, "articles":articles})


def Categories(request, slug_cate = None):
    articles = Article.objects.all()
    if slug_cate is not None:
        category = Category.objects.get(slug = slug_cate)
        articles = Article.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, "category.html", {"categories":categories, "articles":articles})