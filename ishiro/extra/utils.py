from uuid import uuid4
import random


def uuid_generator():
    return uuid4()


def generate_random_digits(n):
    return "".join(map(str, random.sample(range(0, 10), n)))
