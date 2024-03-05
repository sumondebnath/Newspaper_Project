from django import forms
from article.models import Article, Rating


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["user", "category", "headline", "body"]

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     if commit == True:
    #         user.save()
    #         category = self.cleaned_data.get("category")
    #         headline = self.cleaned_data.get("headline")
    #         body = self.cleaned_data.get("body")
    #         image = self.cleaned_data.get("image")

    #         Article.objects.create(
    #             user = user,
    #             category = category,
    #             headline = headline,
    #             body = body,
    #             image = image,
    #         )
    #     return user
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["image"]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]