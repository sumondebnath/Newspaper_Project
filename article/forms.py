from django import forms
from article.models import Article, Rating


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["category", "headline", "body", "image"]
        widgets = {
            "category":forms.Select(attrs={"class":"category-container", "placeholder":"Category"}),
            "headline":forms.TextInput(attrs={"class":"headline-container"}),
            "body":forms.Textarea(attrs={"class":"body-container"}),
            "image":forms.FileInput(attrs={"class":"image-container"}),
        }

    # def save(self, commit=True):
    #     our_user = super().save(commit=False)
    #     if commit:
    #         our_user.user = self.user
    #         our_user.save()
    #     return our_user
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["image"]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]