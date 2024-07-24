from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    contex = {'product': product}
    return render(request, 'catalog/product.html', contex)

