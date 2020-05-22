from django.shortcuts import render
from .models import *

def index(request):
  categories = ItemCategory.objects.all()
  partners = Partners.objects.all()
  sellout = Sellout.objects.all()

  print(categories[4].nestedCategory)

  context = {
    'categories': categories,
    'partners': partners,
    'sellout': sellout,
  }

  return render(request, 'index.html', context=context)

def about(request):
  categories = ItemCategory.objects.all()
  cert = Cert.objects.all()

  context = {
    'categories': categories,
    'cert': cert,
  }

  return render(request, 'about.html', context=context)

def delivery(request):
  categories = ItemCategory.objects.all()
  delivery = Delivery.objects.all()

  context = {
    'categories': categories,
    'delivery': delivery,
  }

  return render(request, 'delivery.html', context=context)

def setup(request):
  categories = ItemCategory.objects.all()

  context = {
    'categories': categories,
  }

  return render(request, 'setup.html', context=context)

def contacts(request):
  categories = ItemCategory.objects.all()

  context = {
    'categories': categories,
  }

  return render(request, 'contacts.html', context=context)