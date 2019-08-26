from django.db import models
from django.urls import reverse
import django
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Post(models.Model):
    """ Model representing a blog post"""
    title = models.CharField(max_length=300) # title model
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)  # used foreign key IS A BLOGGER

    content = models.TextField(help_text="Begin writing...")
    post_date = models.DateField(default=django.utils.timezone.now)

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        """ Returns url for a specific instance of this class. i.e."""
        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        """ Returns string representation of the Post model"""
        return f' {self.title}'

class Comment(models.Model):
    corresponding_post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    content = models.TextField(help_text="Write your comment")
    post_date = models.DateField(default=django.utils.timezone.now)

    commenter = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.commenter}\'s comment on: {self.corresponding_post} at {self.post_date}'


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField( help_text="Some words about yourself...", default="Insert Bio Here...")

    """
    TODO: 
        Do I need this model; can I, instead use the Django.contrib.auth.models -> user
    """
    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.user.id)])

    def __str__(self):
        return f'{self.user}'