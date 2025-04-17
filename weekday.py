# weekday.py
# This program outputs whether or not today is a weekday.
# If this program is run on a Thursday, it will print ' Yes, unfortunately today is a weekday '
# If this program is run on a Saturday, it will print ' It is the weekend, yay! '
# Author : Maroua EL imame

                                            
# import date time library  
import datetime      
# w3schools link below helped me understand Python Datetime and suggested codes for trial.
# reference 5.1 : https://www.w3schools.com/python/python_datetime.asp#:~:text=Try%20it%20%C2%BB-,%25A,Wednesday,-Try%20it%20%C2%BB                                       
x = datetime.datetime.now()     
# this method of formatting (x.strftime("%A") prints the current weekday into a readable string. The method is called strftime()            
# assigning the variable 'today' to its value (the current day)
today = x.strftime("%A")                    

# if and else statements to detect if today's the weekend or a weekday.
if today != " Saturday" or " Sunday":       
    print ("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
