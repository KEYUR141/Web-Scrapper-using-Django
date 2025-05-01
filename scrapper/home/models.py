from django.db import models

# Create your models here.
class IMBD_News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()
    external_link = models.URLField()

class TOI_News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()
    external_link = models.URLField()
    
    

    