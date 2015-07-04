from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Career

def index(request):
    output = Career.objects.all()
    return render_to_response("pathways/index.html")
