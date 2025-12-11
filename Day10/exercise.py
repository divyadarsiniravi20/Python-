from datetime import datetime,date,time,timedelta
#Given a customer’s subscription start date and duration (in days), compute expiry date.
'''
start=date.today()
duration = timedelta(days=15)
end = start + duration
print("Subscription ends on : ",end)'''

#12. Given two dates (start_date, end_date), write a function that returns the number of weekdays.
'''start_date=date(2025,1,1)
end_data=date(2025,1,7)
current=start_date
c=0
while current.weekday()<5:
    c=c+1
    current=current+timedelta(days=1)
print(c)
'''
#print(start_date.weekday())
#You are given a list of attendance timestamps. Count how many fall on a Monday.

'''
def count_mondays(timestamps):
    return sum(ts.weekday()==0 for ts in timestamps)
timestamps=[
    datetime(2025,12,1,9,0),
    datetime(2025,12,2,9,0),
    datetime(2025,12,8,9,0),
]
print(count_mondays(timestamps))'''

#Write a function that checks if a given date is in the future, past, or today.
'''check=date(2025,12,1)
today=date.today()
if today==check:
    print("today")
elif today>check:
    print("Past")
else:
    print("future")'''

#Given a delivery date and expected delivery timeline (like 3 days), calculate estimated deli
# verdate.
'''
delivery_date=date(2025,12,1)
expected_days=3
estimated_date=delivery_date+timedelta(days=3)
print(estimated_date)
'''

#Calculate a user’s precise age (years, months, days) based on DOB.
'''
user_dob=date(2001,1,1)
today=date.today()
years=(today-user_dob).days/365
print(years.__round__())'''

#Write a function that   True if a given year is a leap year.
'''
def leap(year):
    return year%4==0
print(leap(2020))
'''

#Given a list of expiry dates, find which products expire within the next 15 days.
  '''  expiredate=date(2025,5,5)
    dates=[
        date(2025,3,3),
        date(2025,4,4)
    ]
     def expire()
    if date+timedelta(days=15)==expiredate:
        print(dates)
print(expire(date))
'''

