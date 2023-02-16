from django.shortcuts import render, get_object_or_404
from . import models
from .forms import AdoptionDetails
from django.contrib import messages
from django.views import generic, View


# Create your views here.
class AdoptionInfo(generic.ListView):
    model = models.AdoptionQuestions
    template_name = 'adoption/adoption_form.html'
    context_object_name = 'pet_adoption'


def adoption(request):
    adoption = models.AdoptionQuestions.objects.all()
    form = AdoptionDetails(request.POST)
    context = {
        'adoption': adoption,
        'form': form,
    }

    return render(request, 'adoption/adoption_form.html', context)
