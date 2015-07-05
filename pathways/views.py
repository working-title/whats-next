from django.shortcuts import render_to_response, render
from pathways.models import Career, Category, Interest


def index(request):
    categories = Category.objects.all()
    interests = Interest.objects.all()
    return render(request, "pathways/index.html", locals())
