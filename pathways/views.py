from django.http import HttpResponse
from .models import Career, Interest, Qualification

def index(request):
    output = Career.objects.all()
    return HttpResponse(output)
