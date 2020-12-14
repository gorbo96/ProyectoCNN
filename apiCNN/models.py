from django.db import models

class Image(models.Model):
    #https://mc.ai/integrar-modelo-de-red-neuronal-convolucional-en-django/
    # file will be uploaded to MEDIA_ROOT / uploads 
    image = models.ImageField(upload_to ='uploads/') 
    # or... 
    # file will be saved to MEDIA_ROOT / uploads / 2015 / 01 / 30 
    # upload = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    label = models.CharField(max_length=20, blank=True)
    probability = models.FloatField()
