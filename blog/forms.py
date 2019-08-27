from django import forms

from .models import Post, Blogger
from django.contrib.auth.models import User

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        profile = kwargs.get('instance')
        if profile:
            kwargs['instance'] = profile.user

        self.user_form = EditUserForm(*args, **kwargs)

        self.fields.update(self.user_form.fields)
        self.initial.update(self.user_form.initial)

    def save(self, *args, **kwargs):
        self.user_form.save(*args, **kwargs)
        return super(EditProfileForm, self).save(*args, **kwargs)

    class Meta:
        model = Blogger
        exclude = ('user',)
