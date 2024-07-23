from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product1

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product1/', product1, name='product1')
]