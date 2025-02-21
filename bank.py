# bank.py
# this program prints in euros the sum of two amounts in cents
# by Maroua

amount1 = 65
amount2 = 180
amountinCents=amount1+amount2
# or
amountinEuros = (amountinCents)/100

'''
#Method 1
print(f" ¢  {(amountinCents)}  = € {(amount1+amount2)/100}")

print(f" ¢  {(amount1)+(amount2)}  = € {(amount1+amount2)/100}")

# Method 2

print(f" The sum is € {(amount1+amount2)/100}")
print(f" The sum is € {amountinEuros}")

print(f" ¢ {int(amount1)+int(amount2)} is equal to € {(amount1+amount2)/100}")

# Method 3

print(f" ¢ {(amount1+amount2)} is € {(amountinEuros)}")

'''
print(f" The sum of ¢ {(amount1)} +  ¢ {(amount2)} is € {(amount1+amount2)/100}")