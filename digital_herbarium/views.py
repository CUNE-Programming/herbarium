from django.shortcuts import render
from django.views import generic
from camera.forms.forms import PlantImageForm
from digital_herbarium.models import Plant


# Create your views here.
def home(request):
    template_name = "digital_herbarium/home.html"
    context = {}

    return render(request, template_name, context)


class PlantImageFormView(generic.FormView):
    form_class = PlantImageForm
    template_name = "digital_herbarium/base.html"

    def form_valid(self, form: PlantImageForm):
        form.save()
        return super().form_valid(form)
