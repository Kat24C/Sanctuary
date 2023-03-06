from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models
from django.conf import settings
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .forms import MissionForm
from django.contrib import messages


def home_pg(request):
    return render(request, 'sanctuary_home/index.html')


class SanctuaryInfo(generic.ListView):
    model = models.HomePage
    template_name = 'about.html'
    context_object_name = 'sanctuary'


def animal_home_pg(request):
    sanctuary = models.HomePage.objects.all()
    context = {
        'sanctuary': sanctuary,
    }

    return render(request, 'sanctuary_home/about.html', context)


@login_required
def edit_mission(request, info_id):
    edit = get_object_or_404(models.HomePage, pk=info_id)
    if request.user.is_superuser:
        form = MissionForm(request.POST or None, instance=edit)
        if form.is_valid():
            form.save()
            messages.success(request, "Mission statements have been updated")
            return redirect('animals_home_pg')

    else:
        message.error(request, 'Sorry only staff can update the mission.')
        return redirect(reverse('animals_home_pg'))

    context = {
        'form': form,
        'edit': edit
    }

    return render(request, 'sanctuary_home/staff_form.html', context)


def error_404(request, exception):
    return render(request, '404.html')
