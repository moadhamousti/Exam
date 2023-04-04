# Part I: Read Code Written by another Coder 


import random
import string
def function_one(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

function_one(10)
# ============================Modules Imported :========================
# The random : This module Generates pseudo-random numbers.

# Imported string : This Module defines Constants like :

    # 1-ascii_letters
    # 2-ascii_lowercase
    # 3-ascii_uppercase
    # 4-digits
    # 5-punctuation
    # 6-hexdigits
    # 7-octdigits
    # 8-printable
    # 9-whitespace
    

# This code generally generates random characters using ascci letters + digits + ponctuation 
# (using string module).


# This code can be useful in cases where you want to generate a random code , that is hard to be 
# memorized or cracked , for all general uses. 


# we can run the code like this :

function_one(10)

# 10 is the length of the password generated 
    
  