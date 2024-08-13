from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']



class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='product/photo', verbose_name='Фото', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE, related_name="products")
    price_per_purchase = models.DecimalField(max_digits=30, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def  __str__(self):
        return f'{self.name} {self.description} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name',]



class Version(models.Model):
    product = models.ForeignKey(Product, related_name="version", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Продукт")
    version_number = models.IntegerField(verbose_name="Номер версии")
    version_name = models.CharField(max_length=50, verbose_name="Название версии")
    current_version = models.BooleanField(default=True, verbose_name="Признак текущей версии")

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return self.version_name