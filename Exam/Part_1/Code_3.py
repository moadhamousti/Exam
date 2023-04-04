import asyncio
from datetime import datetime, timedelta
from collections import defaultdict
async def is_w(date):
    return date.weekday() >= 5
async def is_h(date):
    holidays = [datetime(2023, 1, 1), datetime(2023, 4, 15), datetime(2023, 5, 1),
datetime(2023, 6, 7), datetime(2023, 9, 16)]
    return date in holidays
async def generater(start_date, end_date):
    dates = defaultdict(list)
    current_date = start_date
    while current_date <= end_date:
        if not await is_w(current_date) and not await is_h(current_date):
            dates[current_date.year].append(current_date)
        current_date += timedelta(days=1)
    return dates
async def main():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    dates = await generater(start_date, end_date)
    year_counts = {year: len(dates[year]) for year in dates}
    print('Number of workdays in 2023:', sum(year_counts.values()))
if __name__ == '__main__':
    asyncio.run(main())
    
    
    
    
# ============================Modules Imported :========================
# In This Code We Imported The asyncio : asyncio library which is used for writing 
# asynchronous code in Python.


# Imported collections : 

# importing the defaultdict class from the collections module.



# Imported datetime : 
    
    
    
# Explaining the Code: 

# 1-defines four functions is_w, is_h, generater. 
# async def is_w(date)/async def is_h(date):
    # --------> is_w: defines a coroutine function takes a date and returns whether the 
        # day of the week for that date is a weekend day (Saturday or Sunday)
    # --------> is_h: defines a coroutine function called is_h that takes in a date and returns whether the date 
    # falls on one of the holidays specified in the function.

# 2- async def main(): 
        # -------> defines a coroutine function called main that initializes the start_date and end_date parameters.
        # -------> generate the dates, and how many workdays for each year. 
        
        
# 3-if __name__ == '__main__':
#     asyncio.run(main():
        # -----------> runs the main coroutine using asyncio.

# Result : finally :prints the total number of work days in 2023.



# This code is used for counting the working days of a given year in this cases :
    # 2023 = 258 
# by eliminating holidays and sundays and maybe saturdays

# it is useful for working people to know how much time they gonna spend with their families each year 






