from django.shortcuts import render, redirect
from article.forms import ArticleForm, ImageForm,RatingForm
from article.models import Article, Rating
from django.views.generic import FormView, View, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class ArticleView(View):
    template_name = "articles.html"
    # form_class = ArticleForm
    # success_url = reverse_lazy("home")
    # def form_valid(self, form):
    #     form.save()
    #     print(form.cleaned_data)
    #     return super().form_valid(form)

    def get(self, request):
        form = ArticleForm()
        return render(request, self.template_name, {"form":form})
    
    def post(self, request):
        if request.method == "POST":
            form = ArticleForm(request.POST)
            # print(request.POST)
            if form.is_valid():
                form.save()
                print(request.POST)
                return redirect("home")
        return render(request, self.template_name, {"form":form})


@login_required
def SetImage(request, id):
    
    if request.method == "POST":
        article = Article.objects.get(id = id)
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            print(request.POST)
            article.image = form.cleaned_data['image']
            article.image.save()
            return redirect("home")
    else:
        form = ImageForm()
    return render(request, "setImage.html", {"form":form})
    

class Details(DetailView):
    model = Article
    pk_url_kwarg = "id"
    template_name = "details.html"

    def post(self, request, *args, **kwargs):
        rating_form =  RatingForm(data=self.request.POST)
        post = self.get_object()
        if rating_form.is_valid():
            new_rating = rating_form.save(commit=False)
            new_rating.article = post
            new_rating.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        ratings = post.ratings.all() # type: ignore
        rating_form = RatingForm()
        
        context["ratings"] = ratings
        context["rating_form"] = rating_form
        return context
    
# def AvarageRating()


class EditArticle(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


@login_required
def DeleteArticle(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect("home")