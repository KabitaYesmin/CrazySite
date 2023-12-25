from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .models import *
from django import forms


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="My Crazy website")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class log_in(models.Model):
    uname = models.CharField(max_length=255)
    psw = models.CharField(max_length=255)

    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None
        return reverse('login')


class Video(models.Model):
    objects = None
    caption = models.CharField(max_length=100)

    video = models.FileField(upload_to="video/%y")


class images(models.Model):
    name = models.CharField(max_length=50)
    Main_Img = models.ImageField(upload_to='images/')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.caption = None

    def __str__(self):
        return (self.caption)

    def is_valid(self):
        pass


class imagesForm(forms.ModelForm):
    class Meta:
        model = images
        fields = ['name', 'Main_Img']
