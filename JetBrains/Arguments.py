def get_percentage(number, round_digits=None):
    perc = round(number * 100, round_digits)
    return f"{perc}%"

print(get_percentage(0.0123, 10))
