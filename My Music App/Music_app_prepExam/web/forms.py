from django import forms

from Music_app_prepExam.web.models import Profile, Album


class ProfileForms(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }

            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age'
                }
            ),

        }



class AddAlbumForms(forms.ModelForm):

    class Meta:

        model = Album
        fields = ('album_name', 'artist_name', 'genre', 'description', 'image_url', 'price')

        widgets = {
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }

            ),
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }

            ),
            'artist_name': forms.TextInput(
                attrs={
                    'placeholder': 'Artist Name',
                }

            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'rows': 3
                }

            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }

            )
        }


class AlbumEditForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('album_name', 'artist_name', 'genre', 'description', 'image_url', 'price')


class AlbumDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('album_name', 'artist_name', 'genre', 'description', 'image_url', 'price')


class DeleteForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()