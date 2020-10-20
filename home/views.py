from django.shortcuts import render
from meals.models import Meals 
from aboutus.models import AboutUs, Why_Choose_Us
from gallery.models import gallery_image
# Create your views here.


def home(request):
    about = AboutUs.objects.all()
    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    why_choose_us = Why_Choose_Us.objects.all()
    gallery = gallery_image.objects.all()


    
    context = {
        'meals' : meals ,
        'meal_list' : meal_list ,
        'why_choose_us' : why_choose_us , 
        'about' : about,
        'gallery' : gallery
    }

    return render(request , 'home/index.html' , context)