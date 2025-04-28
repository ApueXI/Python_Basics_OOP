# print(dir())
# print(__name__)

#if_name == _main_: (this script can be imported OR run standalone)
"""
Functions and classes in this module can be reused without the main block of code executing
Good practice (code is modular,
                helps readability,
                leaves no global variables,
                avoid unintended execution)

Ex. library import library for functionality
When running library directly, display a help page
"""

# asterisk mean everything
# if you want to import a function into a file, you need to put it in a main func, 
# cuz if you import a function from script 1 and run script 2, it will simultaneously run with script 1

# from ifName_isequal_main_TheScript2 import *

def fav_food(food):
    print(f"Your favorite food is {food}")


def main():
    print("This is script 1")
    fav_food("Pizza")
    print("Goodbye")

# means that if you are runnig this file, it will execute this
if __name__ == '__main__':
    main()