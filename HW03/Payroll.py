# File: Payroll.py
# Student: Ryan McWhorter
# UT EID: rcm3369
# Course Name: CS303E
# 
# Date Created: 10 Feb 2021
# Date Last Modified: 
# Description of Program: Homework for week three. Computes an employee's payroll given certain inputs.

def ff(input, non_monetary=True): # format float
    if non_monetary:
        outstr = "{0:.1f}".format(input)
    else:
        outstr = "{0:.2f}".format(input)

    # print(f"[ff]: {outstr}") # for testing purposes.

    idx = outstr.index('.')
    if non_monetary and idx < len(outstr) - 2:
        # we want to append a zero to the string 
        outstr = outstr + "0"
    elif not non_monetary and idx < len(outstr) + 1:
        # we want to append either one or two zeros to the string 
        for _ in range(0,len(outstr) - idx - 3):
            outstr = outstr + "0"
    
    return outstr

# Need to add intermediate rounding to these computations. 
def main():
    print()
    name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked in a week: "))
    rate = float(input("Enter hourly pay rate: "))
    federal_tax_rate = float(input("Enter federal tax withholding rate: "))
    state_tax_rate = float(input("Enter state tax withholding rate: "))

    print(f"\nEmployee Name: {name}")
    print(f"Hours Worked: {ff(hours_worked)}")
    print(f"Pay Rate: ${ff(rate, False)}")
    gp = rate * hours_worked
    print(f"Gross Pay: ${ff(gp, False)}")
    fd = gp * federal_tax_rate
    sd = gp * state_tax_rate
    td = fd + sd
    print(f"Deducations:\n\tFederal Withholding ({ff(federal_tax_rate * 100.0)}%): ${ff(fd, False)}\n\tState Withholding ({ff(state_tax_rate * 100.0)}%): ${ff(sd, False)}\n\tTotal Deduction: ${ff(td, False)}")
    print(f"Net Pay: ${ff(gp - td, False)}")

main() 