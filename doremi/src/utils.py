from datetime import datetime
from dateutil.relativedelta import *

def get_formatted_date(date):
    return f'{date.day:02d}-{date.month:02d}-{date.year}'

def get_validated_date(date):
    day, month, year = [ int(d) for d in date.split('-')]

    if (day > 31 or day < 1) or (month < 1 or month > 12) or (year < 0 or year > 9999):
        print('INVALID_DATE')
        return None
    else:
        return datetime.strptime(date, '%d-%m-%Y').date()

def get_renewal_date(date, months):
    renewal_date = date
    renewal_date += relativedelta(months = months) - relativedelta(days=10)
    return renewal_date