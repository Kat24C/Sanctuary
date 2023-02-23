from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth.models import User
from .forms import AdoptionDetails
from django.contrib import messages
from django.core.mail import BadHeaderError
from django.views import generic, View
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail


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
            message = "hello"

            try:
                send_mail(subject, message, 'ForProjectsKC@gmail.com',
                          ['ForProjectsKC@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid form, Adoption form was not sent')
            messages.success(request, "Adoption form sent, \
                 we will get back to you soon.")
            return redirect('home_pg')

    form = AdoptionDetails()
    return render(request, 'adoption/adoption_form.html', {'form': form})
