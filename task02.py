import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    if min > max:
        raise ValueError("min must be less than max")

    if min < 1:
        raise ValueError("min must be greater than 1")

    if max > 1000:
        raise ValueError("max must be less than 1000")

    if quantity <= 0:
        raise ValueError("quantity must be greater than 0")

    if quantity > max:
        raise ValueError("quantity must be less than max")

    result = []

    while len(result) < quantity:
        number = random.randint(min, max)
        if number in result:
            continue

        result.append(number)

    result.sort()
    return result


try:
    print(get_numbers_ticket(1, 100, 10))
    print(get_numbers_ticket(-1, 100, 200))
except ValueError as err:
    print(err)
