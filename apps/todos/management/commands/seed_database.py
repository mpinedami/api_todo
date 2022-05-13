from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.books.factories import BookFactory
from apps.books.models import Book


class Command(BaseCommand):
    """_summary_

    Args:
        BaseCommand (_type_): _description_

    Raises:
        CommandError: _description_
    """

    help = "Seed database with sample data"

    @transaction.atomic
    def handle(self, *args, **options):
        if Book.objects.exists():
            raise CommandError(
                "This command cannot be run when any question exist, to guard"
                + " against accidental use on production."
            )

        self.stdout.write("Seeding database...")

        create_book()

        self.stdout.write("Done.")


def create_book():
    """
    Create two Question objects and two Choice Objects too
    """
    book1, book2, book3, book4, book5 = BookFactory.create_batch(5)
