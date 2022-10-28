from django.shortcuts import render, redirect

from Music_app_prepExam.web.forms import ProfileForms, AddAlbumForms, AlbumEditForm, AlbumDeleteForm, DeleteForm
from Music_app_prepExam.web.helpers import get_profile, template_action, get_album
from Music_app_prepExam.web.models import Album


# Create your views here.
def show_index(request):
    profile = get_profile()
    albums = get_album()

    if not profile:
        return show_index_with_no_profile(request)

    context = {
        'profile': profile,
        'album': albums,
    }

    return render(request, 'home-with-profile.html', context)

def show_index_with_no_profile(request):
    return template_action(request, ProfileForms, 'index', None, 'home-no-profile.html')


def profile_details(request):
    total_albums = len([albums for albums in get_album()])
    context = {
        'profile': get_profile(),
        'album': total_albums,
    }
    return render(request, 'profile-details.html', context)

def profile_delete(request):
    return template_action(request, DeleteForm, 'index', get_profile(), 'profile-delete.html')


def album_add(request):
    return template_action(request, AddAlbumForms, 'index', None, 'add-album.html')

def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)

def album_edit(request, pk):
    if request.method == 'POST':
        form = AlbumEditForm(request.POST, request.FILES, instance=Album.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlbumEditForm(instance=Album.objects.get(pk=pk))

    context = {
        'form': form,
        'album': Album.objects.get(pk=pk),
        #'expense_slug': get_object_or_404(Expense, pk=pk, slug=slug)
    }
    return render(request, 'edit-album.html', context)

def album_delete(request, pk):
    return template_action(request, AlbumDeleteForm, 'index', Album.objects.get(pk=pk), 'delete-album.html')

