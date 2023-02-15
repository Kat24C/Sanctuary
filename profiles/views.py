from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
# Create your views here.


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')


    form = ProfileForm(instance=profile)

    template = 'profiles/my_profile.html'
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)
