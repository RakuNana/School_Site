from django.forms import ModelForm
from autos.models import Breed

class BreedForm(ModelForm):

    class Meta:

        model = Breed
        fields = "__all__"