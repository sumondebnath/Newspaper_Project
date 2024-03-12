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
from django.views.generic import TemplateView

# Create your views here.

def Home(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles":articles})

class AboutUs(TemplateView):
    template_name = "aboutus.html"

class Contact(TemplateView):
    template_name = "contact.html"