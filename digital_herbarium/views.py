from django.shortcuts import render
from django.views import generic
from digital_herbarium.models import Plant


# Create your views here.
def home(request):
    template_name = "digital_herbarium/home.html"
    context = {}

    return render(request, template_name, context)


