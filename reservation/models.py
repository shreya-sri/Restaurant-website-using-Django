from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    Date = models.DateField()
    time = models.TimeField()
    number_of_persons = models.CharField(max_length=2)
    message = models.TextField()


    def __str__(self):
        return self.name