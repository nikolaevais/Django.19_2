from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class HomeListView(ListView):
    model = Product


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
    template_name = "catalog/contacts.html"

#    def post(self, request):
#        """Метод получения информации со страницы контакты"""
#        if request.method == 'POST':
#            name = request.POST.get('name')
#            phone = request.POST.get('phone')
#            message = request.POST.get('message')
#            print(f'Имя -{name}, телефон - {phone}, сообщение - {message}')
#        return render(request, 'contacts.html')

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory()