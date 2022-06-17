from datetime import datetime

def get_formatted_date(date):
    return f'{date.day:02d}-{date.month:02d}-{date.year}'

def get_validated_date(date):
    day, month, year = [ int(d) for d in date.split('-')]
    if (day > 31 or day < 1) or (month < 1 or month > 12) or (year < 0 or year > 9999):
        print('INVALID_DATE')
        # raise Exception('INVALID_DATE')

    else:
        return datetime.strptime(date, '%d-%m-%Y').date()