"""
URL configuration for newshub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import Home
from django.conf import settings
from django.conf.urls.static import static
# from categories.views import CategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", Home.as_view(), name="home"),
    path("", Home, name="home"),
    path("accounts/", include("account.urls")),
    path("article/", include("article.urls")),
    # path("categorie/", include("categories.urls")),
    # path("categories/", CategoryView, name="category"),
    path("categories/<slug:slug_cate>/", Home, name="category_slug"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)