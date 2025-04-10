from django.shortcuts import render
from django.views import generic
# Create your views here.

def home(request):
    template_name = "camera/home.html"
    context = {}

    return render(request, template_name, context)

def img_process(request):
    template_name = "camera/img_process.html"
    context = {}

    return render(request, template_name, context)

def list(request):
    template_name = "camera/list.html"
    context = {}

    return render(request, template_name, context)