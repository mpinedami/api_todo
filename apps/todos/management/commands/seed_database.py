from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.todos.factories import TodoFactory
from apps.todos.models import Todo


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
        if Todo.objects.exists():
            raise CommandError(
                "This command cannot be run when any todo exist, to guard"
                + " against accidental use on production."
            )

        self.stdout.write("Seeding database...")

        create_todo()

        self.stdout.write("Done.")


def create_todo():
    """
    Create two Question objects and two Choice Objects too
    """
    todo1, todo2, todo3, todo4, todo5 = TodoFactory.create_batch(5)
