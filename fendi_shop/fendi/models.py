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
	size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.CASCADE)
	image = models.ForeignKey(Image, on_delete=models.CASCADE)
	price = models.CharField(max_length=50)
	color = models.ForeignKey(Color, on_delete=models.CASCADE)

	def __str__(self):
		return '{} {}'.format(self.title, self.price)