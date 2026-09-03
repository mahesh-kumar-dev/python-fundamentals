# Python Date Time Module
# Python has a built-in datetime module that helps you work with dates,
# times, and time intervals


'''
    Features:
	Logging -> Record when events happen
	Scheduling -> Run tasks at specific times
	Age calculation -> Compute age from birth date
	Data analysis -> Group data by date/time
	Expiration dates -> Check if something has expired
	Timers -> Measure how long something takes
'''


# The 'datetime' Module

# Importing datetime
import datetime

now = datetime.datetime.now()
print(now)

# import specific classes
from datetime import  datetime, date, time, timedelta

now = datetime.now()
today = date.today()
print(now)
print(today)


# The 'date' Class (just the DATE)
# Creating date objects

from datetime import date

# Create a specific date
birthday = date(2006,1,26)
print(f"My Birth Date: {birthday}")

# Get todays date
today = date.today()
print(f"Today: {today}")

# Get Individual components
print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")


# Date Operations
from datetime import date

# Create dates
new_year = date(2027,1,1)
christmas = date(2026,12,25)
independence = date(1947,8,14)

print(f"New Year: {new_year}")
print(f"Christmas day: {christmas}")
print(f"Independence Date: {independence}")


# Compare dates
print(new_year < christmas)
print(new_year == christmas)

# Calculate Difference
days_until_christmas =   christmas - today
print("Days + time Left for Christmas: ",days_until_christmas)
print("Days Left for Christmas: ",days_until_christmas.days)

# Days of week ( monday = 0 , saturday = 6)
print("Birthday weekday: ",birthday.weekday())
print("Independence weekday: ",independence.weekday())


# Date Formatting
from datetime import date

today = date.today()

# Format as String
print(today.strftime("%Y-%m-%d"))
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%y-%m-%d"))
print(today.strftime("%B %d, %Y"))
print(today.strftime("%d %b, %Y"))
print(today.strftime("%A"))
print(today.strftime("%a"))

# Common format codes
# %Y - Year (4 digits)
# %y - Year (2 digits)
# %m - Month (01-12)
# %d - Day (01-31)
# %B - Full month name (January)
# %b - Abbreviated month name (Jan)
# %A - Full weekday name (Monday)
# %a - Abbreviated weekday name (Mon)


# The 'time' Class (Just the TIME)

# Creating Time Objects
from datetime import time

# Create specific time 
start_time = time(9,30)
end_time = time(17,56,21)
exact = time(14,37,10,68392)

print(start_time)
print(end_time)
print(exact)


# Get Individual Components
t = time(13,30,45)
print(f"Hours: {t.hour}")
print(f"Minutes: {t.minute}")
print(f"Seconds: {t.second}")


# Time operations
from datetime import time, datetime

# Time comparisons (only works if from same day)
morning = time(9,0)
afternoon = time(14,0)
evening = time(19,0)

print(f"Morning: {morning}")
print(f"Afternoon: {afternoon}")
print(f"Evening: {evening}")

print(morning < afternoon)
print(afternoon < evening )

# Combine date and time
from datetime import date, datetime, time

d = date(2026,6,13)
t = time(18,46,58)
dt = datetime.combine(d,t)
print("Date Time: ",dt)


# The 'datetime' Class (Date + Time)

# Creating datetime objects
from datetime import datetime

# Current date and time
now = datetime.now()
print(now)

# Specific Time
covid19 = datetime(2019,12,22,0,0,0)
new_year = datetime(2027,1,1,0,0,0)
print(f"Covid 19: ",covid19)
print(f"New Year: ",new_year)


# Get Individual Component
now = datetime.now()
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hours: {now.hour}")
print(f"Minutes: {now.minute}")
print(f"Seconds: {now.second}")
print(f"Microseconds: {now.microsecond}")


# Extracting date and time
from datetime import datetime

now = datetime.now()

# Get just date
just_date = now.date()
print(f"Just Date: {just_date}")
print(type(just_date))

# Get just Time
just_time = now.time()
print(f"Just Time: {just_time}")
print(type(just_time))



# The 'timedelta' Class (Time Difference)
# timedelta represents a duration – the difference between two dates or times.

from datetime import datetime, timedelta

# Create timedeltas
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
one_hour = timedelta(hours=1)
thirty_minutes = timedelta(minutes=30)

print("One day: ",one_day)
print("One Week: ",one_week)
print("One hour: ",one_hour)
print("Thirty minutes:",thirty_minutes)



# Adding and Subtracting Time
from datetime import datetime , timedelta

now = datetime.now()
print(f"Now: {now}")

# Add time
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

next_week = now + timedelta(weeks=1)
print(f"Next Week: {next_week}")

two_hours_later = now + timedelta(hours=2)
print(f"Two Hour Later: {two_hours_later}")


# Subtract Time
yesterday = now - timedelta(days=1)
print(f"Yesterday: {yesterday}")

one_hour_ago = now - timedelta(hours=1)
print(f"One Hour Ago: {one_hour_ago}")


# Calculating Differences
from datetime import date

# Difference between  dates
start = date(2025,3,17)
end = date(2026,3,17)

diff = end - start 
print(f"Days between: {diff}")
print(f"Total Seconds: {diff.total_seconds()}")


from datetime import datetime

start = datetime(2025,1,1,9,0,0)
end = datetime(2026,1,1,17,30,0)

diff = end - start 
print(f"Hours: {diff.seconds// 3600}")
print(f"Minutes: {(diff.seconds % 3600) // 60}")


# Formatting Dates and Times

# strftime() – Format datetime to string
from datetime import datetime 

now = datetime.now()

# Different Formats
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%B %d , %Y"))
print(now.strftime("%I:%M %p"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%Y-%m-%d  %I:%M:%S"))


'''
Format codes reference
Code	    Meaning	                Example
%Y	        Year (4 digits)	        2024
%y	        Year (2 digits)	        24
%m	        Month (01-12)	        01
%d	        Day (01-31)	            15
%H	        Hour (00-23)	        14
%I	        Hour (01-12)	        02
%M	        Minute (00-59)	        30
%S	        Second (00-59)	        45
%f	        Microsecond	            123456
%p	        AM/PM	                PM
%B	        Full month name	        January
%b	        Abbreviated month	    Jan
%A	        Full weekday	        Monday
%a	        Abbreviated weekday	    Mon
%j	        Day of year (001-366)	015
%w	        Weekday (0=Sunday)	    1
'''


# strptime() – Parse string to datetime

from datetime import datetime

# Parse a string into datetime
date_string = "2024-01-15 14:30:45"
dt = datetime.strptime(date_string,"%Y-%m-%d  %H:%M:%S")
print(dt)

# Different Format
date1 = datetime.strptime("15/01/2023", "%d/%m/%Y")
date2 = datetime.strptime("January 26 , 2006", "%B %d , %Y")
date3 = datetime.strptime("Mon, 15 Jan 2026", "%a, %d %b %Y")

print(date1)
print(date2)
print(date3)


# Practical Example
# Age Calculator
from datetime import date

def calculate_age(birth_date):
    """Calculate age in years"""
    today = date.today()
    age = today.year - birth_date.year
    
    # Check if birthday has occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

# Get birth date from user
year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

birthday = date(year, month, day)
age = calculate_age(birthday)

print(f"You are {age} years old")

# Days until next birthday
today = date.today()
next_birthday = date(today.year, birthday.month, birthday.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_until = (next_birthday - today).days
print(f"Days until next birthday: {days_until}")




# Countdown Timer
from datetime import datetime, timedelta, time

def countdown(target_datetime):
    """Countdown to a specific datetime"""
    while True:
        now = datetime.now()
        remaining = target_datetime - now
        
        if remaining.total_seconds() <= 0:
            print("\nTIME'S UP!")
            break
        
        # Extract days, hours, minutes, seconds
        days = remaining.days
        hours = remaining.seconds // 3600
        minutes = (remaining.seconds % 3600) // 60
        seconds = remaining.seconds % 60
        
        # Display countdown
        print(f"\rCountdown: {days}d {hours:02d}h {minutes:02d}m {seconds:02d}s", 
              end="", flush=True)
        
        time.sleep(1)

# Set target (New Year's Eve)
target = datetime.now()
countdown(target)



# Event Reminder System 
from datetime import datetime, timedelta

class Event:
    def __init__(self, name, date_time):
        self.name = name
        self.date_time = date_time
    
    def days_until(self):
        """Calculate days until event"""
        now = datetime.now()
        diff = self.date_time - now
        return diff.days
    
    def is_today(self):
        """Check if event is today"""
        return self.date_time.date() == datetime.now().date()
    
    def is_upcoming(self, days=7):
        """Check if event is within next X days"""
        now = datetime.now()
        return 0 < self.days_until() <= days
    
    def __str__(self):
        return f"{self.name}: {self.date_time.strftime('%Y-%m-%d %H:%M')}"

# Create events
events = [
    Event("Doctor Appointment", datetime(2024, 2, 15, 10, 30, 0)),
    Event("Project Deadline", datetime(2024, 2, 28, 23, 59, 59)),
    Event("Birthday Party", datetime(2024, 3, 10, 18, 0, 0)),
]

# Check events
print("--- All Events ---")
for event in events:
    print(event)

print("\n--- Today's Events ---")
for event in events:
    if event.is_today():
        print(f"TODAY: {event}")

print("\n--- Upcoming Events (next 30 days) ---")
for event in events:
    days = event.days_until()
    if 0 < days <= 30:
        print(f"{event.name} in {days} days")





# Time Tracker
from datetime import datetime, timedelta, time

class TimeTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.sessions = []
    
    def start(self):
        """Start timing"""
        self.start_time = datetime.now()
        print(f"Started at: {self.start_time.strftime('%H:%M:%S')}")
    
    def stop(self):
        """Stop timing and record session"""
        if self.start_time is None:
            print("No active session")
            return
        
        self.end_time = datetime.now()
        duration = self.end_time - self.start_time
        
        self.sessions.append({
            'start': self.start_time,
            'end': self.end_time,
            'duration': duration
        })
        
        print(f"Stopped at: {self.end_time.strftime('%H:%M:%S')}")
        print(f"Duration: {duration}")
        
        self.start_time = None
    
    def total_time(self):
        """Calculate total time across all sessions"""
        total = timedelta()
        for session in self.sessions:
            total += session['duration']
        return total
    
    def report(self):
        """Display session report"""
        if not self.sessions:
            print("No sessions recorded")
            return
        
        print("\n--- Session Report ---")
        for i, session in enumerate(self.sessions, 1):
            start = session['start'].strftime('%H:%M:%S')
            end = session['end'].strftime('%H:%M:%S')
            duration = session['duration']
            print(f"{i}. {start} -> {end} ({duration})")
        
        total = self.total_time()
        print(f"\nTotal time: {total}")
        print(f"Total hours: {total.total_seconds() / 3600:.2f}")

# Usage
tracker = TimeTracker()

while True:
    print("\n--- Time Tracker ---")
    print("1. Start session")
    print("2. Stop session")
    print("3. View report")
    print("4. Quit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        tracker.start()
    elif choice == "2":
        tracker.stop()
    elif choice == "3":
        tracker.report()
    elif choice == "4":
        break

