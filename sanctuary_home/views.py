from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models
from django.views import generic, View
from .forms import MissionForm


class SanctuaryInfo(generic.ListView):
    model = models.HomePage
    template_name = 'index.html'
    context_object_name = 'sanctuary'


def animal_home_pg(request):
    sanctuary = models.HomePage.objects.all()
    context = {
        'sanctuary': sanctuary,
    }

    return render(request, 'sanctuary_home/index.html', context)


def edit_mission(request):
    return render(request, 'sanctuary_home/staff_form.html')
