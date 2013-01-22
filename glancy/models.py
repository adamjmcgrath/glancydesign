from django.db import models
from google.appengine.api.images import get_serving_url

class Page(models.Model):
  content = models.TextField()
  title = models.CharField(max_length=200)

class HomePic(models.Model):
  position = models.CharField(max_length=5, choices=(('left', 'left'), ('right', 'right')))
  photo = models.ImageField(upload_to=None)
  illustration = models.ImageField(upload_to=None)

  def photo_url(self):
    return get_serving_url(str(self.photo).split('/')[0])

  def illustration_url(self):
    return get_serving_url(str(self.illustration).split('/')[0])