def get_percentage(number, ndigits=None):
    percentage = round(number * 100, ndigits)
    return f'{percentage}%'
