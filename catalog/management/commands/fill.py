from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories_list = [
            {'name': 'auto', 'description': 'for auto'},
            {'name': 'big auto', 'description': 'for big auto'},
            {'name': 'drinks', 'description': 'for drinks'},
        ]
        categories_for_create = []

        for category_item in categories_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)
