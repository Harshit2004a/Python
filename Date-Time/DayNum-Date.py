import datetime

def daynum_to_date(year, day_num):
    try:
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=day_num - 1)
        return date.strftime('%Y-%m-%d')
    except Exception as e:
        return f"Error: {e}"

year = datetime.datetime.now().year
day_num = int(input("Day number: "))
print(daynum_to_date(year, day_num))

# Code by Harshit