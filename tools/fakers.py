import time
from faker import Faker

fake = Faker()

def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

def get_fake_first_name():
    return fake.first_name()

def get_fake_last_name():
    return fake.last_name()