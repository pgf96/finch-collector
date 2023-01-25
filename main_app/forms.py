from django.forms import ModelForm
from .models import *


class NappingForm(ModelForm):
    class Meta:
        model = Napping
        fields = ['date', 'nap']
