# Using random, datetime, and collections :


from datetime import date
import random
import collections

start_date = date.today().replace(day=1, month=1).toordinal()
end_date = date.today().toordinal()

# Random dates
dates = [date.fromordinal(random.randint(start_date, end_date)) for i in range(100)]

# Count the number of times each day of the week appears
day_count = collections.Counter(date.weekday(d) for d in dates)

# Print the results
for day, count in day_count.items():
    print(f"{day}: {count}")
    
    
    
# This is a Python code  generates 100 
# random dates in the current year and counts the number of 
# times each day of the week appears in those dates.


# replace(day=1, month=1) sets it to January 1 of the current year.

