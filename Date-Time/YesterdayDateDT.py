from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)
print("Yesterday's date:", yesterday.strftime('%Y-%m-%d'))

# Code by Harshit