from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories_list = [
            {'name': 'Лампочки', 'description': 'Все виды лампочек'},
            {'name': 'Измерительные приборы',
             'description': 'Приборы для измерения уровней освещенности и шума, напряжения и т.д.'},
            {'name': 'Инструменты', 'description': 'Все виды инструментов'},
        ]

        product_list = [
            {'name': 'Лампочка 7 Ватт',
             'description': 'Светодиодная лампочка, аналог лампы накаливания 60Ватт, свет нейтрально белый',
             'category_id': 1,
             'price': '90'},
            {'name': 'Лампочка 60 Ватт', 'description': 'Обычная лампочка накаливания', 'category_id': 1,
             'price': '19'},
            {'name': 'Мультиметр',
             'description': 'Прибор для "прозвонки" цепей, измерений силы тока, напряжения, сопротивления',
             'category_id': 2, 'price': '600'},
            {'name': 'Люксметр', 'description': 'Прибор для измерения уровня освещенности', 'category_id': 2,
             'price': '3000'},
            {'name': 'Отвертка PH1x100мм',
             'description': 'Отвертка с крестообразным наконечником PH1, длина рабочей части 100мм, '
                            'диэлектрическая ручка',
             'category_id': 3,
             'price': '150'},
            {'name': 'Молоток 500гр',
             'description': 'Молоток весом 500гр, с деревянной ручкой без гвоздодера', 'category_id': 3,
             'price': '150'}
        ]

        for model in (Product, Category):
            model.objects.all().delete()
            table_name = model._meta.db_table

            # сбрасываем счетчик
            with connection.cursor() as cursor:
                query = f"SELECT setval(pg_get_serial_sequence('{table_name}', 'id'), 1, false);"
                cursor.execute(query)

        category_for_create = []
        for category_item in categories_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(Product(**product_item))

        Product.objects.bulk_create(products_for_create)
