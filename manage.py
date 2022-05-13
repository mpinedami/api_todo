#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    argv = sys.argv

    try:
        command = argv[0]
    except IndexError:
        command = "help"

    if command == "test":
        default = "api_todo.settings.test"
    else:
        default = "api_todo.settings.development"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", default)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
