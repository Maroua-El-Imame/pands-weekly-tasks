# acounts.py
# this programs reads in a 10 character account number and outputs the 4 last digits of the added account number
# Author: Maroua EL imame

accountnumber= "1234567890"
accountnumber= input("Enter your account:")
z=accountnumber.replace(accountnumber[0:6] , "xxxxxx")
print("Your account number's 4 last digits : " + z)