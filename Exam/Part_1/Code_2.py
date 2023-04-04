import os
import re
import datetime
def function_two(directory):
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            match = date_pattern.search(filename)
    if match:
        date_str = match.group()
    file_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    year = str(file_date.year)
    month = file_date.strftime('%B')
    new_directory = os.path.join(directory, year, month)
    os.makedirs(new_directory, exist_ok=True)
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(new_directory, filename)
    os.rename(old_path, new_path)
    
    
# ============================Modules Imported :========================
# In This Code We Imported The OS : This module Allows us to use the
# operating system dependent functionality.


# Imported re : 

# Imported datetime : 




# Explaining the Code: 


# 1-Defines a function called function_two 
    
# 2-The re.compile() method returns a pattern object and that matches a date in the 
# format YYYY-MM-DD.

# 3-Loops through each file in the directory using os.listdir(directory) and gives 
# each filename a variable filename.
    # in Directory You specify the disired directory according to you


# 4- Checking if the file is a regular file using os.path.isfile(os.path.join(directory, filename)).
    # -----> If the file is a regular file, searches for a match for the pattern using match = date_pattern.search(filename).
        # ------> If a match is found, extracts the matched date using match.group() .
    # (used two consucutive if statements in the code)
    
# 5- Difining variables :
    # ------> file_date: date of the file
    # ------> Year: the year
    # ------> month: the month
    # ------> new_directory: Creates a new directory with the path using os.path.join(directory, year, month)
    # ------> old_path: assigns this variable to directory and old path
    # ------> new_path: assigns this variable to directory and new path
    



# ====================This Code Used For:=========================


# This code renames files in the selected directory :
#     ------> extracting the date from the filename 
#     ------> creating a new directory with the date extracted. 
#     ------> moves the file to the new directory while you can rename it.














