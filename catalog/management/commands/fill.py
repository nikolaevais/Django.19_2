import json
import os

from django.core.management import BaseCommand

from catalog.models import Product, Category
from config.settings import BASE_DIR


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """получаем данные из фикстуры с категориями"""
        with open('catalog/fixtures/catalog_category_data.json', encoding="UTF-8") as file:
            categories = json.load(file)
        return categories


    @staticmethod
    def json_read_products():
        """получаем данные из фикстуры с продуктами"""
        with open('catalog/fixtures/catalog_product_data.json', encoding="UTF-8") as file:
            products = json.load(file)
        return products


    def handle(self, *args, **options):

        Product.objects.all().delete()          # Удалите все продукты
        Category.objects.all().delete()        # Удалите все категории


        product_for_create = []               # Создайте списки для хранения объектов
        category_for_create = []              # Создайте списки для хранения объектов

				# Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id= category["pk"], name=category["fields"]["name"], description=category["fields"]["description"]))


        Category.objects.bulk_create(category_for_create)        # Создаем объекты в базе с помощью метода bulk_create()

				# Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(id= product["pk"],
                        name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        price_per_purchase=product["fields"]["price_per_purchase"],
                        created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"])
            )

        Product.objects.bulk_create(product_for_create)          # Создаем объекты в базе с помощью метода bulk_create()