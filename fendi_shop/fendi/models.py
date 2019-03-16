from django.db import models

# Create your models here.


class Image(models.Model):
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.image_url


class Size(models.Model):
    size_name = models.CharField(max_length=120)

    def __str__(self):
        return self.size_name


class Color(models.Model):
    color_name = models.CharField(max_length=120)

    def __str__(self):
        return self.color_name


class ItemShop(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    size = models.ManyToManyField(
        Size, null=True, blank=True)
    image = models.ManyToManyField(Image, null=True, blank=True)
    price = models.CharField(max_length=50)
    color = models.ManyToManyField(Color, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.price)
