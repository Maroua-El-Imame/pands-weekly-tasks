# es.py
# This program reads in a text file and outputs the number of e's it contains.
# when program runs using the python file name only, it redirects user to use the correct command
# The program should take the filename from an argument on the command line. 
# requirements : dealing with errors eg no argument, filename that does not exist, or is not a text file.

# Author : Maroua EL imame 

# assumptions: 
# if the file doesnt exist this will definitely throw an error that we will need to handle and again prompt user to use a file that exists.
# if a file exists but not in the roght format '.txt', user needs to be redirected to use the proper format.
# we can create a file, but if a complex heavy file not stored in the folder/repository, it would not be possible to create it again  and use it in a timely manner.
# following the Weekly task 07 : the ouptput is :
            #$ python es.py moby-dick.txt
            # 116960
# in the weekly task, I can see in the input ' moby-dick.txt ', this is not a local file and sure enough I can't run it, I needed to learn more about thsi texte file.
# upon searching the web, we can download the file and store it in the same folder/repo where the program is located, and go grom there.
# I started by typing then understanding the file use, then look up to download the Plain Text UTF-8 format which I saved under file name : moby-dick.txt , file format: txt file.
# I then moved the file into the same folder where the python script (es.py) is located
# file accessible through the link bellow :
# url:https://www.gutenberg.org/ebooks/2701


# Importing built-in libraries
import sys          # This lets us read arguments from the command line
import os.path      # This lets us check if the file exists ! also applied functions in lab07-files of programming module 


# url: https://docs.python.org/3/library/os.path.html#:~:text=os.path.isfile,for%20the%20same%20path.
# this resource helped me check the python documentation and learn more about the os.path.isfile 

if not os.path.isfile('moby-dick.txt'):
    print ("File does not exist")

# creating a function that will return the number of e's in a file.
def count_e(filename):
    try:
        # if condition to check if the file ends with '.txt'
        if not filename.endswith('.txt'):
            # program returns the following if it's not a .txt, to make sure the right file format is used.
            raise ValueError("Not a text file. Please enter a '.txt' file")  

        # try to open read the file
        #'with' will make sure the file is closed after being opened and used. by this, we make sure that we can open the file without a problem in the future.
        # we open the file path of 'filename', in 'r' read mode, using the UTF-8 format, which will decode the letters using the UTF-8 format,in case there are accents or special characters.
        # url: https://www.w3schools.com/charsets/ref_html_utf8.asp
        # url: https://www.smashingmagazine.com/2012/06/all-about-unicode-utf8-character-sets/
        with open(filename, 'r', encoding='utf-8') as f:
            # Read the full file
            content = f.read()  
            # convert all text to lowercase and count 'e', methods explained through the following links 
            # url:https://www.w3schools.com/python/ref_string_lower.asp
            # url:https://www.w3schools.com/python/ref_string_count.asp
            count = content.lower().count('e')
            # Show the number of e’s
            print(count)  

    # except to handle errors
    # NotFoundError a python built-in exception, I used the link bellow to learn more about this module.
    # url: https://docs.python.org/3/library/exceptions.html#:~:text=exception%20ModuleNotFoundError%C2%B6
    

    except FileNotFoundError:
        print("Error: File does not exist.")
        # ve for value error which could be any other error type
    except ValueError as ve:
        # print the messaage with the error as it's shown
        print(f"Error: {ve}")  
        # this catches any error that wasn’t already caught by previous specific error types
    except Exception as e:
        print(f"Unexpected error: {e}") 

# This runs first when type: python es.py filename.txt
if __name__ == "__main__":
    # checks if the user typed the filename also checks whether we entered at least two elements
    #'sys.argv' is a list (from the sys module) that stores all the arguments passed from the command line when you run your Python script. more infos used from this link bellow:
    # url:https://docs.python.org/3/library/sys.html
    if len(sys.argv) != 2:
         # this guides the user to the right number of elements to be used, in this case 2 : the name of the python file and the argument
         # this will make sure this script runs only when we call it directly
        print(input(f"file format accepted : es.py moby-dick.txt "))
    else:
        count_e(sys.argv[1])  


