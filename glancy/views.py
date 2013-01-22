from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Page, HomePic

def home(request):
  return render_to_response('glancy/home.html', {
    'page': Page.objects.get(title='Home'),
    'left':  HomePic.objects.get(position='left'),
    'right':  HomePic.objects.get(position='right')
  })

def about(request):
  return render_to_response('glancy/about.html', {'page': Page.objects.get(title='About')})

def portfolio(request):
  return render_to_response('glancy/portfolio.html', {'page': Page.objects.get(title='Portfolio')})

def pricing(request):
  return render_to_response('glancy/pricing.html', {'page': Page.objects.get(title='Pricing')})

def suppliers(request):
  return render_to_response('glancy/suppliers.html', {'page': Page.objects.get(title='Suppliers')})

def contact(request):
  return render_to_response('glancy/contact.html', {'page': Page.objects.get(title='Contact')})