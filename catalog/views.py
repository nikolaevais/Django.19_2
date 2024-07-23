from django.shortcuts import render

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home_list.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def product1(request):
    return render(request, 'product1.html')
