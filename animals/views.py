from django.shortcuts import render

# Create your views here.

def animal_home_pg(request):
    return render(request, 'animals/index.html')