from django.db import models

# Create your models here.
class gallery_image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title