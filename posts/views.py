from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.

class HomePageView(ListView):
    model = models.Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'