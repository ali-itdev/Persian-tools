from __init__ import SETTINGS, get_data


def is_leap(year: int, type: str = 'g'):
    
    # types :
    #     g => gregorian
    #     j => jalali
    #     h => hijri

    type = type[0].lower() # get only first index of the whole word 

    if type == 'g' and year % 4 == 0:
        return True
    if type == 'j' and year % 4 == 3:
        return True
    return False


def gregorian_to_jalali(day: int, month: int, year: int):
    # Converting the year
    jalali_year = None
    if year >= 622:
        jalali_year = year - 621
    else:
        return 'Unexpected year'
    # Check valid date and Convert all months to day => 17/2 => 30+28+17
    if day <= 31 and month <= 12:

        months_days_number = None
        isleap = is_leap(year)

        if isleap:
            months_days_number = (31,29,31,30,31,30,31,31,30,31,30,31)
        else:
            months_days_number = (31,28,31,30,31,30,31,31,30,31,30,31)

        # Counting the number of days before this month 
        gregorian_days_count = 0
        for i in range(month - 1):
            gregorian_days_count += months_days_number[i]
        gregorian_days_count += day
        

        # Diffrences beetwen gregorian and jalali new years
        jalali_days = gregorian_days_count - 79
        
        # Find n number in a year
        month_count = 1
        while jalali_days > 29:
            if month_count <= 6:
                jalali_days -= 31
            else:
                jalali_days -= 30
            month_count += 1

        resault = {
            'year':jalali_year,
            'month': month_count,
            'day': jalali_days
        }
        return resault
    return 'Unexpected days/month'


