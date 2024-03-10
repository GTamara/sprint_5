import random
import string


def generate_random_string(length: int) -> str:
    letters = string.ascii_lowercase + string.digits
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_password(length: int) -> str:
    return generate_random_string(length)


def generate_email(length: int) -> str:
    return generate_random_string(length) + '@yandex.ru'
