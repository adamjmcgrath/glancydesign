from django.db import models
from google.appengine.api import images

class Page(models.Model):
  content = models.TextField(blank=True)
  subcontent = models.TextField(blank=True)
  title = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='about', blank=True)

  def photo_url(self):
    return images.get_serving_url(str(self.photo).split('/')[0])

class HomePic(models.Model):
  position = models.CharField(max_length=5, choices=(('left', 'left'), ('right', 'right')))
  photo = models.ImageField(upload_to='home/photo')
  illustration = models.ImageField(upload_to='home/illustration')

  def photo_url(self):
    return images.get_serving_url(str(self.photo).split('/')[0])

  def illustration_url(self):
    return images.get_serving_url(str(self.illustration).split('/')[0])

class Supplier(models.Model):
  name = models.CharField(max_length=200)
  link = models.URLField()

class PortfolioPhoto(models.Model):
  photo = models.ImageField(upload_to='portfolio')
  title = models.CharField(max_length=200)

  def photo_url(self):
    return images.get_serving_url(str(self.photo).split('/')[0])

class Pricing(models.Model):
  position = models.IntegerField()
  description = models.CharField(max_length=200)
  cost = models.CharField(max_length=200)
