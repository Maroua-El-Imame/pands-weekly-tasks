# bank.py
# this program prints in euros the sum of two amounts in cents
# Author: Maroua EL imame

# Asking user to enter a first amount then 2nd amount in cents
# int so the amount is read as intger not as string.
amount1  = int(input(" Please enter the first  amount in cents : "))
amount2  = int(input(" Please enter the second amount in cents : "))   

# sum of two amounts
amountinCents=amount1+amount2

# sum of amounts in cents when devided by 100 return the amount in euros.
amountinEuros = (amountinCents)/100

# result
print(f" The total of amounts you entered is € {amountinEuros}")
