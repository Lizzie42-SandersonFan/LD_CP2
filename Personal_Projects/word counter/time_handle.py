# LD 1st file for getting time stamp for Word Counter
from datetime import datetime
from zoneinfo import ZoneInfo

# Note by time I mean that on ANOTHER page you need to write the code that gets the current time and cleans it up to print out in the format that you need. 

# Function for getting time and formating to be put at the end of the file (via file_handle). Need to know what the current year, month, day, hour, minute, and second are and format it as 'Last Updated at: year-month-day at hour-minute-second'
def get_time():
    now_utah = datetime.now(ZoneInfo("America/Denver"))
    formatted_datetime = now_utah.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_datetime
