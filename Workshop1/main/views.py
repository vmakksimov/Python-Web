from django.shortcuts import render, redirect

from Workshop1.main.models import Profile, PetPhoto


# Create your views here.

def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None

def show_home(request):
    context = {
        'hide_context' : True,
    }
    return render(request, 'home_page.html', context)


def dashboard_view(request):
    profile = get_profile()
    pets = PetPhoto.objects\
        .filter(tagged_pets__user_profile=profile)

    context = {
        'pets': pets,

    }
    return render(request, 'dashboard.html', context)



def profile_view(request):
    return render(request, 'profile_details.html')


def photo_view(request, pk):

    pet_photo = PetPhoto.objects.get(pk=pk)
    context = {
        'pet_photo': pet_photo
    }
    return render(request, 'photo_details.html', context)


def like_pet(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo', pk)