from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from .forms import AdoptionDetails
from django.contrib import messages
from django.views import generic, View


# Create your views here.
@login_required
class AdoptionInfo(generic.ListView):
    model = models.AdoptionQuestion
    template_name = 'adoption/adoption_form.html'
    context_object_name = 'pet_adoption'


@login_required
def adoption(request):
    adoption = models.AdoptionQuestion.objects.all()
    form = AdoptionDetails(request.POST)
    context = {
        'adoption': adoption,
        'form': form,
    }

    return render(request, 'adoption/adoption_form.html', context)
