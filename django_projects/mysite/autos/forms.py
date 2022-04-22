from django.forms import ModelForm
from autos.models import Make



#Make a class that inherits a Model Form, This grabs the named model and makes it a form.
#In this case it's grabbing my Make model from autos.models. Var in class mete needs to be "model" ModelForm will look for that name
#The fields var tells ModeForms to find all the fields and return them


class MakeForm(ModelForm):

    class Meta:

        model = Make
        fields = "__all__"