from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('',views.image_list , name='image_list' ),
]