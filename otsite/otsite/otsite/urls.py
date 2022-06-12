"""otsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from pages.views import home_view, about_view, activities_view, brothers_view, rush_view, contact_view
from brothers.views import brother_create_view
from accounts.views import RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('about/', about_view),
    path('activities/', activities_view),
    path('brothers/', brothers_view),
    path('rush/', rush_view),
    path('contact/', contact_view),
    path('create/', brother_create_view),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
