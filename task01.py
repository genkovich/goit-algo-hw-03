from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date")
        return

    today = date.today()
    diff = date - today
    return diff.days


example_date_with_positive_diff = "2025-01-01"
result = get_days_from_today(example_date_with_positive_diff)
print(result)

example_date_with_negative_diff = "2023-01-01"
result = get_days_from_today(example_date_with_negative_diff)
print(result)

error_format = "02/01/2025"
result = get_days_from_today(error_format)
print(result)
