from django.conf.urls.defaults import patterns, url

from glancy import views

urlpatterns = patterns('glancy.views',
  ('^about/?', 'about'),
  ('^portfolio/?$', 'portfolio'),
  ('^pricing/?$', 'pricing'),
  ('^suppliers/?$', 'suppliers'),
  ('^contact/?$', 'contact'),
  url(r'^$', 'home'),
)

