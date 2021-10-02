import math
from __init__ import SETTINGS, get_data
from datetime import datetime
from .ummalqura_arrray import UmalqurraArray

this_year = datetime.now().year


def is_leap(year: int, type: str = 'g'):

    # types :
    #     g => gregorian
    #     j => jalali
    #     h => hijri

    type = type[0].lower()  # get only first index of the whole word

    if type == 'g' and year % 4 == 0:
        return True
    if type == 'j' and year % 4 == 3:
        return True
    return False


def gregorian_to_jalali(day: int, month: int, year: int = this_year):
    # Converting the year
    jalali_year = None
    if year > 621:
        jalali_year = year - 621
    else:
        return 'Unexpected year'
    # Check valid date and Convert all months to day => 17/2 => 30+28+17
    if day <= 31 and month <= 12:

        months_days_number = None
        isleap = is_leap(year)

        if isleap:
            months_days_number = (31, 29, 31, 30, 31, 30,
                                  31, 31, 30, 31, 30, 31)
        else:
            months_days_number = (31, 28, 31, 30, 31, 30,
                                  31, 31, 30, 31, 30, 31)

        # Counting the number of days before this month
        gregorian_days = 0
        for i in range(month - 1):
            gregorian_days += months_days_number[i]
        gregorian_days += day

        # Diffrences between gregorian and jalali new years

        if gregorian_days > 79:
            jalali_days = gregorian_days - 79

            # Find n number in a year
            month_count = 1
            while jalali_days > 29:
                if month_count <= 6:
                    jalali_days -= 31
                else:
                    jalali_days -= 30
                month_count += 1

        else:
            jalali_year -= 1

            diff = 79 - gregorian_days

            jalali_days = None

            month_count = 12

            if diff < 29:
                jalali_days = 29 - diff
            elif diff > 29 and diff < 59:
                jalali_days = 59 - diff
                month_count -= 1
            else:
                jalali_days = 79 - diff if gregorian_days > 20 else gregorian_days + 10
                month_count -= 2

        if month <= 3 and is_leap(jalali_year, 'j'):
            jalali_days += 1

        resault = {
            'year': jalali_year,
            'month': month_count,
            'day': jalali_days
        }
        return resault
    return 'Unexpected days/month'


def gegorean_to_hijri(day, month, year = this_year):
    # This code the modified version of R.H. van Gent Code, it can be found
    # at http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm
    # read calendar data
    day = int(day)
    m = int(month)  # Here we enter the Index of the month (which starts with Zero)
    y = int(year)
    # append January and February to the previous year (i.e. regard March as
    # the first month of the year in order to simplify leapday corrections)
    if m < 3:
        y -= 1
        m += 12
        # determine offset between Julian and Gregorian calendar
    a = math.floor(y / 100.)
    jgc = a - math.floor(a / 4.) - 2
    # compute Chronological Julian Day Number (CJDN)
    cjdn = math.floor(365.25 * (y + 4716)) + \
        math.floor(30.6001 * (m + 1)) + day - jgc - 1524
    a = math.floor((cjdn - 1867216.25) / 36524.25)
    # compute Modified Chronological Julian Day Number (MCJDN)
    mcjdn = cjdn - 2400000
    # the MCJDN's of the start of the lunations in the Umm al-Qura calendar are stored in 'islamcalendar_dat.js'
    index = UmalqurraArray.get_index(mcjdn)
    # compute and output the Umm al-Qura calendar date
    iln = index + 16260
    ii = math.floor((iln - 1) / 12)
    iy = ii + 1
    im = iln - 12 * ii
    id = mcjdn - UmalqurraArray.ummalqura_dat[index - 1] + 1
    
    resault = {
        'year': iy,
        'month': im,
        'day': id
    }
    return resault


def get_events(day: int, month: int):
    if day <= 31 and month <= 12:

        jalali_date = gregorian_to_jalali(day, month)

        sameMonth = []
        events = []
        data = None

        path = ['gregorian.json', 'jalali.json']
        for p in range(len(path)):
            dir = SETTINGS['calendar_path'] + '/' + path[p]
            data = get_data(dir)
            data = data['events']

            # switch to jalali date
            if p == 1:
                day = jalali_date['day']
                month = jalali_date['month']

            # Search in data by month key

            for i in range(len(data)):
                data_month = data[i]['month']
                if data_month == month:
                    sameMonth.append(data[i])

            # Search in data by day key

            for i in range(len(sameMonth)):
                data_day = sameMonth[i]['day']
                if data_day == day:
                    events.append(sameMonth[i])

        return events
    return 'Unexpected days/month'
