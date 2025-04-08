from django.urls import path
from . import views

app_name = "camera"
urlpatterns = [
    path("home", views.home),
    path("img_process", views.img_process),
    
]
