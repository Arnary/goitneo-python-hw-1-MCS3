from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    happy_days = defaultdict(list)
    current_day = datetime.today().date()
    for user in users:
        user_Bday = user["birthday"]
        user_Bday = datetime.date(user_Bday)
        birthday_this_year = user_Bday.replace(year=current_day.year)

        if birthday_this_year < current_day:
            birthday_this_year = birthday_this_year.replace(
                year=current_day.year+1)
        delta_days = (birthday_this_year - current_day).days

        if delta_days < 7:
            day_of_the_week = birthday_this_year.strftime("%A")
            if day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
                if birthday_this_year > current_day:
                    continue

                happy_days["Monday"].append(user["name"])
                continue
            happy_days[day_of_the_week].append(user["name"])

    show_bd(happy_days)


def show_bd(happy_days):
    result = list()
    for day, names in happy_days.items():
        L = str()
        L += day + ": "
        for name in names:
            L += name + ", " if name != names[-1] else name
        result.append(L)
    print("\n".join(result))
