"""
forms.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Define reusable forms for the chirper app.

"""

from django import forms
from digital_herbarium.models import Plant


class PlantImageForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ["image"]
        widgets = {
            "image": forms.FileInput(attrs={"accept": "image/*"}),
        }
