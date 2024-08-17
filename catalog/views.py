from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class HomeListView(ListView):
    model = Product

    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data()
        version_dict = {}
        products = context_data['products']
        for product in products:
            product_version = Version.objects.filter(product=product, current_version=True).first()
            version_dict[product.name] = product_version
        context_data['current_versions'] = version_dict
        return context_data



class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')






class ContactsView(TemplateView):
    """Класс для вывода страницы с контактами"""
    template_name = "catalog/contacts.html"

