# acounts.py
# this programs reads in a 10 character account number and outputs its last 4 digits
# it also reads in account number of any length and outputs its last 4 digits.
# Author: Maroua EL imame

# Asking user to enter a 10 characters account number, not specifically digits. 
accountnumber= input("Please enter an account number of 10 characters : ")

# string replace method allows to replace the first 6 digits with xxxxxx    
# I used the reference below to understand and apply slicing From the start & string replace method
# reference 3.1 : https://www.w3schools.com/python/python_strings_slicing.asp#:~:text=Slice%20From%20the%20Start 
# reference 3.2 : https://www.w3schools.com/python/ref_string_replace.asp

# assigning a variable
secure_account_number=accountnumber.replace(accountnumber[0:6] , "xxxxxx")      

# print
print("The account number's 4 last characters : " +str(secure_account_number)) 

#-------------------

# user input
randomnumber= input("Please enter an account number of any length : ")

# using the reference below, I could learn more and practice slicing and negative indexing.
# negative indexing reverses the slice and helps selecting items without needing to know the exact length of the list. 
# in this case, the slice starts at index 0 and ends until the 4th index from the end of the string is reached. The slice of any length is replaced by xxxxxx 
# reference 3.3 : https://www.w3schools.com/python/python_strings_slicing.asp#:~:text=Try%20it%20Yourself%20%C2%BB-,Negative%20Indexing,-Use%20negative%20indexes
# reference 3.4 : https://www.w3schools.com/python/ref_string_replace.asp
# reference 3.5 : https://stackoverflow.com/questions/509211/how-slicing-in-python-works#:~:text=part%20explains%20them.-,Negative%20indexes,-The%20very%20first

# assigning a variable
secure_random_account_number=randomnumber.replace(randomnumber[:-4],"xxxxxx")  

# print
print("The account number's 4 last digits : " + str(secure_random_account_number))            
                                                                     
