from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    today = datetime(2024, 1, 15).date() #today = datetime.now().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        tmp_birthday_date = birthday.replace(year=today.year)
        days_until_birthday = tmp_birthday_date - today
        if 7 >= days_until_birthday.days >= 0:
            if tmp_birthday_date.weekday() == 6:
                tmp_birthday_date += timedelta(days=1)
            elif tmp_birthday_date.weekday() == 5:
                tmp_birthday_date += timedelta(days=2)

            tmp_data = {
                'name': user['name'],
                'congratulation_date': tmp_birthday_date.strftime('%Y.%m.%d'),
            }
            upcoming.append(tmp_data)

    return upcoming


users = [

    {"name": "John Doe", "birthday": "1985.01.22"},
    {"name": "John Saturday", "birthday": "1985.01.20"},
    {"name": "Jane Smith", "birthday": "1990.01.16"},
    {"name": "Jack Doe", "birthday": "1991.01.15"},
    {"name": "Jack Doe", "birthday": "1992.01.12"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
