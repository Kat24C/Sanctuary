from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .forms import PetDetails
from django.contrib import messages


class PetInfo(generic.ListView):
    model = models.AboutTheAnimal
    template_name = 'animals_basic.html'
    context_object_name = 'pets'


def animal_outline(request):
    pets = models.AboutTheAnimal.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'animals/animals_basic.html', context)


def wild_animals(request):
    return render(request, 'animals/animals_basic.html')


def farm_animals(request):
    return render(request, 'animals/animals_basic.html')


def pets(request):
    return render(request, 'animals/animals_basic.html')
