from factory import Faker
from factory.django import DjangoModelFactory

from .models import Todo


class TodoFactory(DjangoModelFactory):
    class Meta:
        model = Todo

    title = Faker("sentence", nb_words=3)
    body = Faker("sentence", nb_words=20)
