# Collatz.py
# This program asks the user to enter a positive integer.
# The next value is calculated by taking the number entered, then depending on the value :
# if value is even, the program divide the inserted value by 2
# if it is odd, the program then multiplies the inserted value by 3 and adds 1 ]
# The program ends when the current value is one.
# Author : Maroua EL imame
         

# def : defining the function 
def collatz(number):  

    # even number : defined by the value entered, when devided the remainder is equal to 0 
    if number % 2 == 0:   
        # when even number is entered, it calculates the value of the number divided by 2                      
        evenNumberResult=number//2   
        # the append() method will add the number result to the end of a list           
        numberList.append(evenNumberResult)     
        # return statement it tells the function what value should be returned
        return(evenNumberResult)    
    # not even number = odd number            
    elif number % 2 != 0:       
        # when odd number is entered, it calculates the value of the number multiplied by 3 then adding 1                 
        oddNumberResult = 3 * number + 1     
        # the append() method will add the number result to the end of a list   
        numberList.append(oddNumberResult)  
        # return statement it tells the function what value should be returned    
        return(oddNumberResult)                 

      
# Assigning a value to the user input to simplify the print 
number = int(input('Please enter a positive integer : '))    
numberList = [number]      

# The program runs in loop as long as the statement is True. The program, then ends when number 1 is finally reached ( statement is False)
while number != 1:                              
            number = collatz(int(number))
else:
         print(numberList)
        
# The program outputs the following :
# Please enter a positive integer : 10
# 10 5 16 8 4 2 1

# reference 4.1 : https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff#:~:text=37-,def%20collatz(number)%3A,-if%20number%20%25
# this resource was very informative and helpful to understand the collatz code.
