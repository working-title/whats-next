from django.shortcuts import render_to_response, render
from taggit.models import Tag
from pathways.models import Career, Category, Interest


def index(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    interests = Interest.objects.all()
    return render(request, "pathways/index.html", locals())

def subjects(request):
    categories = Category.objects.all()
    interests = Interest.objects.all()
    return render(request, "pathways/subjects.html", locals())