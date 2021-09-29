from __init__ import SETTINGS, get_data

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


def gregorian_to_jalali(day: int, month: int, year: int):
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

        if month <= 3 and is_leap(jalali_year,'j'):
            jalali_days +=1
        
        resault = {
            'year': jalali_year,
            'month': month_count,
            'day': jalali_days
        }
        return resault
    return 'Unexpected days/month'