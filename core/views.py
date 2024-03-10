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

def Home(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles":articles})