from django.shortcuts import render
from django.http import HttpResponse

from brothers.models import Brother
    
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def activities_view(request, *args, **kwargs):
    return render(request, "activities.html", {})

def brothers_view(request, *args, **kwargs):
    obj = Brother.objects.all()
    context = {
        'object': obj
    }

    return render(request, "brothers.html", context)

def rush_view(request, *args, **kwargs):
    return render(request, "rush.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
