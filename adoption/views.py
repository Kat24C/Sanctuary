from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import AdoptionDetails
from django.contrib import messages
from django.core.mail import BadHeaderError
from django.views import generic, View
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail

from . import models


# Create your views here.
@login_required
class AdoptionInfo(generic.ListView):
    model = models.AdoptionQuestion
    template_name = 'adoption/adoption_form.html'
    context_object_name = 'pet_adoption'


@login_required
def adoption(request):
    adoption = models.AdoptionQuestion.objects.all()
    if request.method == 'POST':
        form = AdoptionDetails(request.POST)
        if form.is_valid():
            subject = "Adoption Details"
            adoption = {
                'perspective_pet_parent': form.cleaned_data['perspective_pet_parent'],
                'User_email': form.cleaned_data['User_email'],
                'other_pets': form.cleaned_data['other_pets'],
                'please_give_details': form.cleaned_data['please_give_details'],
                'what_type_of_pet': form.cleaned_data['what_type_of_pet'],
                'pet_you_want': form.cleaned_data['pet_you_want'],
                'where_will_the_pet': form.cleaned_data['where_will_the_pet'],
            }
            message = "\n".join(adoption.values())

            try:
                send_mail(subject, message, 'ForProjectsKC@gmail.com', ['ForProjectsKC@gmail.com '])
            except BadHeaderError:
                return HttpResponse('Invalid form, Adoption form was not sent')
                messages.success(request, "Adoption form sent, \
                we will get back to you soon.")
            return redirect("../sanctuary_home/index.html")
    form = AdoptionDetails()
    return render(request, 'adoption/adoption_form.html', {'form': form})
