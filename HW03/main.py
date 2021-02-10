# File: Payroll.py
# Student: Ryan McWhorter
# UT EID: rcm3369
# Course Name: CS303E
# 
# Date Created: 10 Feb 2021
# Date Last Modified: 
# Description of Program: Homework for week three. Computes an employee's payroll given certain inputs.

# Need to add intermediate rounding to these computations. 
def main():
    name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked in a week: "))
    rate = float(input("Enter hourly pay rate: "))
    federal_tax_rate = float(input("Enter federal tax withholding rate: "))
    state_tax_rate = float(input("Enter state tax withholding rate: "))

    print(f"\nEmployee Name: {name}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Pay Rate: {rate}")
    gp = rate * hours_worked
    print(f"Gross Pay: {gp}")
    fd = gp * federal_tax_rate
    sd = gp * state_tax_rate
    td = fd + sd
    print(f"Deducations:\n\tFederal Withholding ({federal_tax_rate * 100.0}%): ${fd}\n\tState Withholding ({state_tax_rate * 100.0}%): ${sd}\n\tTotal Deduction: ${td}")
    print(f"Net Pay: ${gp - td}")

main() 