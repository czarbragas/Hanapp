"""NOCSApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from ITAssetManager.views import HomeView, RegisterView, AccountCreateView
from ITAssetManager.tables.accounts import AccountListView, AccountDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    # path('register/', RegisterView.as_view()),
    path('register/', AccountCreateView.as_view()),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('contact/', TemplateView.as_view(template_name="contact.html")),
    # path('accounts/<slug:slug>', AccountListView.as_view()),
    path('accounts/', AccountListView.as_view()),
    path('accounts/<slug:slug>', AccountDetailView.as_view()),
] 
