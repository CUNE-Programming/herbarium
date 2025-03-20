from django.urls import path
from . import views

app_name = "digital_herbarium"
urlpatterns = [
    path("home", views.home),
]
