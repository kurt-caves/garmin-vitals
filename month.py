from init_connect import MyCredentials
from garminconnect import Garmin
import calendar

def get_month_stats(month :str) -> str:
    if month.lower() == 'jan':
        month = '01'
    elif month.lower() == 'feb':
        month = '02'
    elif month.lower() == 'mar':
        month = '03'
    elif month.lower() == 'apr':
        month = '04'
    elif month.lower() == 'may':
        month = '05'
    elif month.lower() == 'jun':
        month = '06'
    elif month.lower() == 'jul':
        month = '07'
    elif month.lower() == 'aug':
        month = '08'
    elif month.lower() == 'sep':
        month = '09'
    elif month.lower() == 'oct':
        month = '10'
    elif month.lower() == 'nov':
        month = '11'
    elif month.lower() == 'dec':
        month = '12'
    return month

def get_days(year: str, month: str) -> int:
    start_day, days = calendar.monthrange(int(year), int(month))
    return days
    

def main() -> None:
    garmin = Garmin(MyCredentials().email,MyCredentials().password)
    garmin.login()
    today_stats = garmin.get_stats('2024-10-2')
    print(type(today_stats))
    for key, value in today_stats.items():
        print(key, value)
if __name__ == '__main__':
    month = get_month_stats('JAN')
    year = '2024'
    days = get_days(year, month)
    print("days in jan ", days, type(days))
    print(month, type(month))
    # main()
    garmin = Garmin(MyCredentials().email,MyCredentials().password)
    garmin.login()
    for day in range(days):
        day_as_str=str(day+1)
        day_str = (year+"-"+month+"-"+day_as_str)
        print(day_str)
        today_stats = garmin.get_stats(day_str)
        print(type(today_stats))
        for key, value in today_stats.items():
            print(key, value)


