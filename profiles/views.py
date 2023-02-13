from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
# Create your views here.


def profile(request):
    """ Display the user's profile. """
#    profile = get_object_or_404(Profile, user=request.user)

#    if request.method == 'POST':
#        form = ProfileForm(request.POST, instance=profile)
#        if form.is_valid():
#            form.save()
# #           messages.success(request, 'Profile updated successfully')
#
#    form = ProfileForm(instance=profile)
#
#    template = 'profiles/profile.html'
#    context = {
#        'form': form,
#    }

    return render(request, 'profiles/my_profile.html')
