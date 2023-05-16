from faker import Faker

fake = Faker('ru_RU')
Faker.seed()

print(fake.first_name())