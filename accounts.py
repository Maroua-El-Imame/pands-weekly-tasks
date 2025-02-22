# acounts.py
# this programs reads in a 10 character account number and outputs the account number with only the last 4 digits showing.
# Author : Maroua El imame


accountnumber= "1234567890"


z=accountnumber.replace("123456" , "xxxxxx")

enter10digitsaccountnumber = input("Enter your account number:")
print(z)