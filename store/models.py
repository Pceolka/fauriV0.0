from django.db import models
from django.contrib.auth.models import User


# Создание моделей


class News(models.Model):
    date = models.CharField(max_length=25)
    desc = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='media/')
    headertext = models.CharField(max_length=25, default="")
    fulldesc = models.CharField(max_length=200, default="")
    image_1 = models.ImageField(upload_to='media/')
    image_2 = models.ImageField(upload_to='media/')
    image_3 = models.ImageField(upload_to='media/')
    date_2 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date

