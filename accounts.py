# acounts.py
# this programs reads in a 10 character account number and outputs its last 4 digits
# it also reads in account number of any length and outputs its last 4 digits, too.
# Author: Maroua EL imame


accountnumber= str("1234567890")
accountnumber= input("Enter your account number of 10 digits:")
z=accountnumber.replace(accountnumber[0:6] , "xxxxxx")
print("Your account number's 4 last digits : " +str(z))

# resources of solution 1 : 
# Slicing From the Start & string replace () method
# url : https://www.w3schools.com/python/python_strings_slicing.asp#:~:text=Slice%20From%20the%20Start
# url : https://www.w3schools.com/python/ref_string_replace.asp


randomnumber = "1236547896541236654478963225"
randomnumber= input("Enter yout account number of any length: ")
y=randomnumber.replace(randomnumber[:-4],"xxxxxx")
print("Your account number's 4 last digits : " + str(y))

# resources of solution 2 : negative indexing & string replace () method
# url : https://www.w3schools.com/python/python_strings_slicing.asp#:~:text=Try%20it%20Yourself%20%C2%BB-,Negative%20Indexing,-Use%20negative%20indexes
# url : https://www.w3schools.com/python/ref_string_replace.asp
