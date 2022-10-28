from django.shortcuts import redirect, render

from Music_app_prepExam.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


def get_album():
    expenses = Album.objects.all()
    if expenses:
        return expenses
    else:
        return None


def template_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
        'album': instance,
    }
    return render(request, template_name, context)