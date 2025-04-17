# squareRoot.py
# a 'sqrt' function.
# this program takes a positive floating-point number as input and outputs an approximation of its square root.
# this program is not using python built-in functions x**5 or math.sqrt(x)
# Author : Maroua EL imame

# steps :
#   1. understand the question
#   What's a square root ?
#   a square root of a number is a value that can be multiplied by itself to give the original number.

#   2. identify the arguments needed for the calculation
#    we need the result(number) to which we try and find its square root(a number when multiplied by itself gives the result(number))

#   3. what's the desired outcome ?
#   The square root of a result(number)

#   Example : 
#   The square root of a number is a value that, when multiplied by itself, gives the original number. 
#   In other words: We know that 5 × 5 = 25, in this case, the square root of 25 is 5.

#   steps to identify the square root.

#   4. Identify resources: Resources used to emplement the Newton method into python

# reference 6.1 : https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# this resource was mainly used to find the accurate Newton method formula, it also explains the different parameters to use.

# reference 6.2 : https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.02-Tolerance.html + AI generated explanation on Bing browser.
# keywords searched "(N, guess, tolerance) explained for python " 
# This resource explains the tolerance principle as used in engineering application. 

# reference 6.3 : https://codepal.ai/code-generator/query/ZMi7XfSJ/python-square-root-newtons-method
# reading and understanding the code

# ---------------------------

# 5. Implementing the solution.
# Newton method :

# defining the function sqrt
# sqrt  : Compute the square root of a given number using the Newton method.
# n     : the number whose square root is to be found. 
def sqrt(n):
    
    # initial approx: start with an initial approximate, often half of the number.
    approx = n / 2  
    
    while True:
        # implementing method ;  root = 0.5 * (x + (n / x))
        better_approx = 0.5 * (approx + (n / approx))  

        # tolerance check: Continue iterating until the absolute difference is less than the tolerance.
        # in other words: 1e-10( pr 0.0000000001) is a very small number that ensures the result is accurate to at least 10 decimal places.
        # we can adjust the tolerance level (to 1e-5 for example) depending on how fast and how precise we want the result to be.
        if abs(better_approx - approx) < 1e-10:
            # return The new approximate square root of n.
            return better_approx 
        
        # update the approximation for the next iteration
        approx = better_approx

# get user input and ensure it's a valid positive float number
while True:
    try:
        n = float(input("Enter a positive number: "))
        if n <= 0: # excluding 0 too, as it returns an error when entered by user. 
            print("Please enter a new positive number.(do not use negative numbers or 0)")
        else:
            break  # exit loop if input is valid
    except ValueError:
        print("Invalid number. Please enter a valid number.")

# calculate and display the square root
# assigning a variable to the function.
result = sqrt(n)

# print the result
print(f"The square root of {n} is approximately {result}")

