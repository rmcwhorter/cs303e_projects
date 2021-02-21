# File: DaysInMonth.py
# Student: Ryan McWhorter
# UT EID: rcm3369
# Course Name: CS303E
# 
# Date Created: 20 Feb 2021
# Date Last Modified: 20 Feb 2021
# Description of Program: Homework for week four. Computes the number of days in a month.

def month(year, month):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        return 31 
    elif (month == 2): # is leap year?
        if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
            return 29 # yes its a leap year
        else:
             return 28 # no, its not a leap year
    else:
        return 30

def match_year(year): # I missed this part -> "Don't use lists or other Python constructs not yet covered in class though week 4."
    return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][year - 1]

def match_year_compliant(year): # uglier but compliant
    if year == 1:
        return "January"
    elif year == 2:
        return "February"
    elif year == 3:
        return "March"
    elif year == 4:
        return "April"
    elif year == 5:
        return "May"
    elif year == 6:
        return "June"
    elif year == 7:
        return "July"
    elif year == 8:
        return "August"
    elif year == 9:
        return "September"
    elif year == 10:
        return "October"
    elif year == 11:
        return "November"
    elif year == 12:
        return "December"

def main():
    year = int(input("Please enter a year: ")) 
    mth = int(input("Please enter a month: ")) 
    print(f"{match_year_compliant(mth)} {year} has {month(year, mth)} days")

main() 