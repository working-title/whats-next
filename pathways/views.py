from django.shortcuts import render_to_response, render, get_object_or_404
from taggit.models import Tag
from pathways.models import Career, Category, Interest, Industry


def index(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    interests = Interest.objects.all()
    return render(request, "pathways/index.html", locals())


def subjects(request, industry_pk):
    industry = get_object_or_404(Industry, pk=industry_pk)
    careers = industry.careers
    return render(request, "pathways/subjects.html", locals())