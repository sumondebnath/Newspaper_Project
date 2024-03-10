from django.urls import path
from categories.views import Categories

urlpatterns = [
    path("category/<slug:slug_cate>/", Categories, name="category_slug"),
    path("category/", Categories, name="categories"), 
]