from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ItemShop(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    size = models.ManyToManyField(Size)
    image = models.ManyToManyField(Image)
    price = models.CharField(max_length=50)
    color = models.ManyToManyField(Color)

    def __str__(self):
        return '{} {}'.format(self.title, self.price)
