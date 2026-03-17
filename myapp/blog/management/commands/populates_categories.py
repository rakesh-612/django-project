from blog.models import Category
from django.core.management.base import BaseCommand
from typing import Any


class Command(BaseCommand):
    help = "This command inserts categories data"

    def handle(self, *args: Any, **options: Any):

        Category.objects.all().delete()  # Delete existing datas

        categories = ['Sports', 'Technology', 'Science', 'Art', 'Food']

        for category_name in zip(categories):
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS(
            "Completed categories inserting data!"))
