from django.urls import path
from article.views import ArticleView, Details, EditArticle, DeleteArticle, SetImage

urlpatterns = [
    path("article/", ArticleView, name="article"),
    path("details/<int:id>/", Details.as_view(), name="detail"),
    path("edit-article/<int:id>/", EditArticle.as_view(), name="edit_article"),
    path("delete-article/<int:id>/", DeleteArticle, name="delete_article"),
    path("set-image/<int:id>/", SetImage, name="set_image"),
]