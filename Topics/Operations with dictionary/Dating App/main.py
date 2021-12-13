def select_dates(potential_dates):
    confirmed_date_names = []
    for date in potential_dates:
        if date["age"] > 30 and "art" in date["hobbies"] and date["city"] == "Berlin":
            confirmed_date_names.append(date["name"])
    return f'{", ".join(confirmed_date_names)}'
