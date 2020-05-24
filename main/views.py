from django.shortcuts import render
from .models import *

def index(request):
  categories = ItemCategory.objects.filter(nestedCategory=None)
  partners = Partners.objects.all()
  sellout = Sellout.objects.all()

  print(categories[0])

  context = {
    'categories': categories,
    'partners': partners,
    'sellout': sellout,
  }

  return render(request, 'index.html', context=context)

def about(request):
  categories = ItemCategory.objects.filter(nestedCategory=None)
  cert = Cert.objects.all()

  context = {
    'categories': categories,
    'cert': cert,
  }

  return render(request, 'about.html', context=context)

def delivery(request):
  categories = ItemCategory.objects.filter(nestedCategory=None)
  delivery = Delivery.objects.all()

  context = {
    'categories': categories,
    'delivery': delivery,
  }

  return render(request, 'delivery.html', context=context)

def setup(request):
  categories = ItemCategory.objects.filter(nestedCategory=None)

  context = {
    'categories': categories,
  }

  return render(request, 'setup.html', context=context)

def contacts(request):
  categories = ItemCategory.objects.filter(nestedCategory=None)

  context = {
    'categories': categories,
  }

  return render(request, 'contacts.html', context=context)

def sale(request):
  categories = ItemCategory.objects.filter(nestedCategory=None)
  items = Item.objects.filter(cost_sale__gt=0)

  context = {
    'categories': categories,
    'items': items,
  }

  return render(request, 'sale.html', context=context)

def category(request, pk):
  categories = ItemCategory.objects.filter(nestedCategory=None)
  category = ItemCategory.objects.get(id=pk)
  items = Item.objects.filter(kind=category)

  context = {
    'categories': categories,
    'title': category.title,
    'items': items,
  }

  return render(request, 'category.html', context=context)

def search(request):
  categories = ItemCategory.objects.filter(nestedCategory=None)
  query = request.GET.get('query')
  items = Item.objects.filter(title__icontains=query)

  context = {
    'categories': categories,
    'query': query,
    'items': items,
  }

  return render(request, 'search.html', context=context)