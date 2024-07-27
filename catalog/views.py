from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class HomeListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


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


