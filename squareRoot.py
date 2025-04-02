# squareRoot.py
# creating 'sqrt' function.
# This program takes a positive floating-point number as input and outputs an approximation of its square root.
# This program is not using python built-in functions x ** .5 or math.sqrt(x)

# Author : Maroua EL imame

# steps :
#   1. understand the question:
#   What's a square root ?
#   The square root of a number is a number that when multiplied by itself gives the actual number.

#   2. Identify the arguments needed for the calculation.
#    we need the result(number) to which we try and find its square root(a number when multiplied by itself prooducts the result(number))

#   3. what's the desired outcome ?
#   The square root of a result(number)

#   Example : 
#   The square root of a number is a value that, when multiplied by itself, gives the original number. 
#   In other words: We know that 5 × 5 = 25, in this case, the square root of 25 is 5.
#   Let's find out how to identify the square root.

#   4. Identify resources: Resources used to emplement the Newton method into python

# link1: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# This source was mainly used to find the accurate Newton method formula, it also explains the different parameters used.
# link2: https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.02-Tolerance.html + AI generated explanation on Bing browser.
# Keywords searched "(N, guess, tolerance) explained for python " 
# This resource explains the tolerance principle as used in engineering application. 
# link3: https://codepal.ai/code-generator/query/ZMi7XfSJ/python-square-root-newtons-method
# reading and understanding the codec



# ---------------------------
# 5. Implementing the solution.
# Newton method :

# defining the function sqrt
# sqrt      : Compute the square root of a given number using the Newton-Raphson method.
# n         : the number whose square root is to be found. 

def sqrt(n):
    
    # Initial approx: start with an initial approximate, often half of the number.
    approx = n / 2  
    
    while True:
        # implementing method ;  root = 0.5 * (x + (n / x))
        
        better_approx = 0.5 * (approx + (n / approx))  
        # Tolerance Check: Continue iterating until the absolute difference is less than the tolerance.
        # in other words: 1e-10( pr 0.0000000001) is a very small number that ensures the result is accurate to at least 10 decimal places.
        # we can adjust the tolerance level (to 1e-5 for example) depending on how fast and how python s    precise we want the result to be.
        
        if abs(better_approx - approx) < 1e-10:
            # return The new approximate square root of n.
            return better_approx 
        
        # Update the approximation for the next iteration
        approx = better_approx

# Get user input and ensure it's a valid positive number
while True:
    try:
        n = float(input("Enter a positive number: "))
        if n <= 0: # excluding 0 too, as it returns an error when entered by user. 
            print("Please enter positive number.(do not use negative numbers or 0)")
        else:
            break  # Exit loop if input is valid
    except ValueError:
        print("Invalid number. Please enter a valid number.")

# calculate and display the square root
# assigning a variable to the function.
result = sqrt(n)
# Last print the result
print(f" The square root of {n} is approximately {result}")

