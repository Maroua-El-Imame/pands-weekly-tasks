# Collatz.py
# This program asks the user to enter a positive integer.
# The next value is calculated by taking the number entered, then depending on the value :
# if value is even [the program divide the named value by 2
# if it is odd [ the program multiplies the odd number by 3 and adds 1 ]
# The program ends when the current value is one.

# Author : Maroua EL imame



                                                # Variables and Values explained :          


def collatz(number):                            # def : defining the function                                                         

    if number % 2 == 0:                         # even number : defined by the value entered, when devided the remainder is equal to 0 
        evenNumberResult=number//2              # when even number is entered, it calculates the value of the number divided by 2
        numberList.append(evenNumberResult)     # the append() method will add the number result to the end of a list
        return(evenNumberResult)                # return statement it tells the function what value should be returned
    elif number % 2 != 0:                       # not even number = odd number
        oddNumberResult = 3 * number + 1        # when odd number is entered, it calculates the value of the number multiplied by 3 then adding 1 
        numberList.append(oddNumberResult)      # the append() method will add the number result to the end of a list
        return(oddNumberResult)                 # return statement it tells the function what value should be returned

# Program starts here.        

number = int(input('Please enter a positive integer : '))    # Variable
numberList = [number]                                        # Numbers list
        
while number != 1:                              # The program runs in loop as long as the statement is True. The program, then ends when number 1 is finally reached ( statement is False)
            number = collatz(int(number))
else:
         print(numberList)
        
# The program outputs the following :
# Please enter a positive integer : 10
# 10 5 16 8 4 2 1

# Resources:
# url : https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff#:~:text=37-,def%20collatz(number)%3A,-if%20number%20%25
# elif statement edited to match the program condition
