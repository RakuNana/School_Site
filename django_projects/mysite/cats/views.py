from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView , DeleteView, UpdateView
from django.urls import reverse_lazy

from cats.models import Breed , Cat

# Create your views here.

class MainView(LoginRequiredMixin, View):

    def get(self, request):

        c = Cat.objects.all()
        b = Breed.objects.all().count()

        context = {"breed_count" : b , "cat_list" : c}

        return render(request , "cats/cats_list.html" , context)


class CatView(LoginRequiredMixin, View):

    def get(self, request):

        kl = Breed.objects.all()
        context = {"breed_list" : kl}

        return render(request , "cats/breed_list.html" , context)


class CatCreate(LoginRequiredMixin, CreateView):

    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('kitten:all')

class CatUpdate(LoginRequiredMixin, UpdateView):

    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('kitten:all')

class CatDelete(LoginRequiredMixin, DeleteView):

    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('kitten:all')



class BreedCreate(LoginRequiredMixin, CreateView):

    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('kitten:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):

    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('kitten:all')


class BreedDelete(LoginRequiredMixin, DeleteView):

    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('kitten:all')
