# from django.shortcuts import render
# from django.views.generic import TemplateView
# from categories.views import CategoryView

# # Create your views here.

# # class Home(TemplateView):
# #     CategoryView()
# #     template_name = "index.html"

# def Home(request):
#     CategoryView(request)
#     return render(request, "index.html")


from django.shortcuts import render
from categories.models import Category
from article.models import Article

# Create your views here.

def Home(request, slug_cate = None):
    articles = Article.objects.all()
    if slug_cate is not None:
        category = Category.objects.get(slug = slug_cate)
        articles = Article.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, "index.html", {"categories":categories, "articles":articles})