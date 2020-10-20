from django.shortcuts import render

# Create your views here.
from .models import gallery_image 

def image_list(request):
    image_list = gallery_image.objects.all()

    context = {
        'image_list' : image_list ,
    }

    return render(request , 'gallery/list.html' , context)
# Create your views here.
