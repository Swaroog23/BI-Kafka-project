from random import randint
from typing import Dict

from faker import Faker

fake = Faker()


def generate_user() -> Dict:
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": randint(18, 60),
        "city_address": fake.city(),
    }


if __name__ == "__main__":
    print(generate_user())
