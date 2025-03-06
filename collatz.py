# Collatz.py
# This program asks the user to insert any positive integer and outputs the values 10 5 16 8 4 2 1
# The principle of calculation : The next value is calculated by taking the current value, if 
#  value is even [divide it by 2], if it is odd [multiply it by 3 and add on]. The program end if the current value is one.



number = int(input("enter an integer:"))

if (number % 2) == 0:
    print (number//2)
else:
    print((3*number)+1)

# Need more details how to insert append so the numbers are kept for the end, and then displayed as a serie.

