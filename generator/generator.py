from data.data import Person
from faker import Faker
import random

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 88),
        department=faker_ru.job(),
        email=faker_ru.email(),
        salary=random.randint(1000, 5000),
        current_address=faker_ru.address(),
        permament_address=faker_ru.address()
    )