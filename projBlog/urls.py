"""projBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings                                  #include static and media folders for displaying images
from appArticle import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', article_views.article_list, name='home'),            #by default redirect user to Article create page
    path('appArticle/', include('appArticle.urls')),              #include url file from appArticle, because this the main project
    path('accounts/', include('accounts.urls')),                  #include accounts url from accounts app
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                    #finding media url from settings file