from django.shortcuts import render, Http404, get_object_or_404
from django.shortcuts import reverse, redirect
from . import models
from django.core.paginator import Paginator
from django.views import generic, View
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import PetDetails
from django.contrib import messages


class PetInfo(generic.ListView):
    model = models.AboutTheAnimal
    template_name = 'animals_basic.html'
    context_object_name = 'pets'


def animal_outline(request):
    pets = models.AboutTheAnimal.objects.all().order_by('id')
    query = None
    num = Paginator(pets, 8)
    page = request.GET.get('page')
    page_num = num.get_page(page)
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('pet_info'))

            queries = Q(type_of_animal__icontains=query)
            pets = pets.filter(queries)

    context = {
        'pets': page_num,
        'search_term': query,
        'page_num': page_num,
    }
    return render(request, 'animals/animals_basic.html', context)


def pet_info(request, pet_id):
    pet = get_object_or_404(models.AboutTheAnimal, pk=pet_id)

    context = {
        'pet': pet
    }
    return render(request, 'animals/pet_info.html', context)


@login_required
def add_pet(request):
    """ Add a new pet to the sanctuary """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff members can add new pets')
        return redirect(reverse('animals_home_pg'))

    if request.method == 'POST':
        new_pet = PetDetails(request.POST, request.FILES)
        if new_pet.is_valid():
            pet = new_pet.save()
            messages.success(request, 'A new pet has joined the sanctuary!')
            return redirect(reverse('animal_outline'))
        else:
            messages.error(request, 'A new pet has not been add.')

    else:
        new_pet = PetDetails()

    context = {
        'new_pet': new_pet,
    }

    return render(request, 'animals/pet_add.html', context)


@login_required
def edit_pet(request, pet_id):
    """ Add a new pet to the sanctuary """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff members can access this!')
        return redirect(reverse('animals_home_pg'))

    try:
        pet = models.AboutTheAnimal.objects.get(pk=pet_id)
    except AboutTheAnimal.DoesNotExist:
        messages.error(request, 'Sorry this did not work')
        raise Http404("Oops. Sorry something went wrong.")

    if request.method == 'POST':
        pet_edit = PetDetails(request.POST, request.FILES, instance=pet)
        if pet_edit.is_valid():
            pet_edit.save()
            messages.success(request, f'You have edited the \
details of {pet.animals_name}')
            return redirect(reverse('animal_outline'))
    else:
        pet_edit = PetDetails(instance=pet)
        messages.info(request, f'You are changing the \
details of {pet.animals_name}')

    context = {
        'pet': pet,
        'pet_edit': pet_edit,
    }

    return render(request, 'animals/animals_edit.html', context)


def delete_pet(request, pet_id):
    """ Add a new pet to the sanctuary """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff members can access this!')
        return redirect(reverse('animals_home_pg'))

    try:
        pet = models.AboutTheAnimal.objects.get(pk=pet_id)
    except AboutTheAnimal.DoesNotExist:
        messages.error(request, "Oops. Sorry something went wrong.")
        raise Http404("Oops. Sorry something went wrong.")

    if request.method == "POST":
        pet.delete()
        messages.success(request, 'This pet has been adopted.')
        return redirect(reverse('animal_outline'))

    context = {
        'pet': pet,
    }

    return render(request, 'animals/delete_pet.html', context)

