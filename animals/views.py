from django.shortcuts import render


def animals(request):
    return render(request, 'animals/animals.html')


def wild_animals(request):
    return render(request, 'animals/wild_animals.html')


def farm_animals(request):
    return render(request, 'animals/farm_animals.html')


def pets(request):
    return render(request, 'animals/pets.html')
