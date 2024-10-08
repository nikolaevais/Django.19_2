from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_category_from_cache


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



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)




class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')



    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.is_unpublish_product") and user.has_perm("catalog.change_description_product") and user.has_perm("catalog.change_category_product"):
            return ProductModeratorForm
        raise PermissionDenied



class ContactsView(TemplateView):
    """Класс для вывода страницы с контактами"""
    template_name = "catalog/contacts.html"


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_category_from_cache()
