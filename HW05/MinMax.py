# File: MinMax.py
# Student: Ryan McWhorter
# UT EID: rcm3369
# Course Name: CS303E
# 
# Date Created: 21 Feb 2021
# Date Last Modified: 21 Feb 2021
# Description of Program: Homework for week five. The min-max homework.

def main():
    val = input("Enter an integer or 'stop' to end: ")
    accumulator = []
    while val != "stop":
        accumulator.append(int(val))
        val = input("Enter an integer or 'stop' to end: ")
    if len(accumulator) > 0:
        print(f"The maximum is {max(accumulator)}")
        print(f"The minimum is {min(accumulator)}")
    else: 
        print("You didn't enter any numbers")

main()