# This program outputs whether or not today is a weekday.
# If this program is run on a Thursday, it should print ' Yes, unfortunately today is a weekday '
# If this program is run on a Saturday, it should print ' It is the weekend, yay! '

# Author : Maroua EL imame

                                            

import datetime                             # import date time library                   
x = datetime.datetime.now()                 # using the following method of formatting (x.strftime("%A") which will print the current Weekday into a readable string.The method is called strftime()
today = x.strftime("%A")                    # assigning the variable today to its value (the current day)
    
if today != " Saturday" or " Sunday":       # if and else statements to detect if today's the weekend or a weekday.
    print ("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")


# Resources used:
# url: https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_a2
# url : https://www.w3schools.com/python/python_datetime.asp#:~:text=Try%20it%20%C2%BB-,%25A,Wednesday,-Try%20it%20%C2%BB
