from django.db import models

# Create your models here.

class QRCodeImage(models.Model):
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media")

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return self.image
