import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(num: str) -> str:
    UA_CODE = '38'

    num = re.sub('[^0-9]+', '', num)
    if num.startswith(UA_CODE):
        num = f"+{num}"
    elif len(num) == 10:
        num = f"+{UA_CODE}{num}"
    else:
        raise ValueError(f"Invalid phone number: {num}")

    return num


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
