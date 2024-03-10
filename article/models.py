from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from article.constants import RATINGS

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="media/article/images/", null=True, blank=True)

    def __str__(self):
        return self.headline
    

class Rating(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="ratings")
    rating = models.CharField(max_length=10, choices=RATINGS) 
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.rating