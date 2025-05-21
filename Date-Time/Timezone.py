from datetime import datetime
import pytz

timezones = ['UTC', 'US/Eastern', 'Europe/London', 'Asia/Kolkata', 'Australia/Sydney']

for tz_name in timezones:
    tz = pytz.timezone(tz_name)
    current_time = datetime.now(tz)
    print(f"Current time in {tz_name}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
# Code by Harshit