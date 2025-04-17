# es.py
# this program reads in a text file and outputs the number of e's it contains.
# when program runs using the python file name only, it redirects user to use the correct command
# the program should take the filename from an argument on the command line. 
# requirements : dealing with errors eg no argument, filename that does not exist, or is not a text file.
# Author : Maroua EL imame 

# assumptions: 
# if the file doesnt exist this will definitely throw an error that we will need to handle, then again, prompt user to use a file that exists.
# if a file exists but not in the right format '.txt', user will need to be directed to use the proper format.
# users can create files, but if a complex heavy file not stored in the folder/repository, it would not be possible to create it again and use it in a timely manner.

# following the Weekly task 07 of programming and scripting module, the ouptput is :
            #$ python es.py moby-dick.txt
            # 116960

# in the weekly task, I can see in the input ' moby-dick.txt ', this is not a local file and sure enough I can't run it, I needed to learn more about this texte file.
# upon searching the web, there were available resources to download the file.
# it was suggested to download the Plain Text UTF-8 format (the use of this format is explained later in the code) which I saved under file name : moby-dick.txt , file format: txt file.
# I then moved the file into the same folder where the python script (es.py) is located
# file downloadable through the link bellow :
# reference 7.1 :https://www.gutenberg.org/ebooks/2701


# importing built-in libraries
# This module read arguments from the command line
import sys          
# This module checks if the file exists. I applied functions explained in lab07-files of programming and scripting learning module 
import os.path      

# applying the methods proposed in programming and scripting 'topic07-files.ipynb' 

# reference 7.2 : https://docs.python.org/3/library/os.path.html#:~:text=os.path.isfile,for%20the%20same%20path.
# this resource helped me check the python documentation and learn more about the os.path.isfile 
if not os.path.isfile('moby-dick.txt'):
    print ("File does not exist")

# creating a function that will return the number of e's in a file.
def count_e(filename):
    try:
        # if condition to check if the file ends with '.txt'
        if not filename.endswith('.txt'):
            # program returns the following if it's not a .txt, in order to redirect the user to use the right file format.
            # reference 7.3 : https://docs.python.org/3/tutorial/errors.html#:~:text=8.4.%20Raising%20Exceptions%C2%B6
            raise ValueError("Not a text file. Please enter a '.txt' file")  

        # try to open read the file
        # 'with' will make sure the file is closed after being opened and used, this avoids any file opening issues in future.
        # I opened the file path of 'filename', in 'r' read mode, using the UTF-8 format, which will decode the letters using the UTF-8 format in case of presence of accents or special characters.
        # reference 7.4 : https://www.w3schools.com/charsets/ref_html_utf8.asp
        # reference 7.5 : https://www.smashingmagazine.com/2012/06/all-about-unicode-utf8-character-sets/
        # reference 7.6 : https://pythonhow.com/how/read-a-text-file-with-python/
        with open(filename, 'r', encoding='utf-8') as f:
            # read the full file
            content = f.read()  
            # convert all text to lowercase and count 'e', methods explained through the following links 
            # reference 7.7 :https://www.w3schools.com/python/ref_string_lower.asp
            # reference 7.8 :https://www.w3schools.com/python/ref_string_count.asp
            count = content.lower().count('e')
            # Show the number of e’s
            print("This file contains" , count , "e's")  

    # except to handle errors
    # NotFoundError a python built-in exception, I used the link below to understand this module.
    # reference 7.9 : https://docs.python.org/3/library/exceptions.html#:~:text=exception%20ModuleNotFoundError%C2%B6
    except FileNotFoundError:
        print("Error: File does not exist.")
        # ve for value error which could be any other error type
    except ValueError as ve:
        # print the messaage with the error as it's shown in output
        print(f"Error: {ve}")  
        # this catches any error that wasn’t already caught by previous specific error types
    except Exception as e:
        print(f"Unexpected error: {e}") 

# This runs first when user types python es.py filename.txt
if __name__ == "__main__":
    # checks if the user typed the filename also checks whether we entered at least two elements
    #'sys.argv' is a list (from the sys module) that stores all the arguments passed from the command line when user runs a Python script. More infos used from this link below:
    # reference 7.10 : https://docs.python.org/3/library/sys.html
    if len(sys.argv) != 2:
         # this guides the user to the right number of elements to be used, in this case 2 : the name of the python file and the argument
         # this will make sure this script runs only when user calls it directly
        print(input(f"file format accepted : es.py moby-dick.txt "))
    else:
        count_e(sys.argv[1])  


