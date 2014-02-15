# Assignment 2: Write a Python script that generates the nth sequence
# of the Fibonacci numbers. The script will take exactly one command
# line argument for n.
# filename : fibonacci.py
# Author: Garth
import sys
# Things to do:
#   First: dummy guard. Cant allow input that is not a non-negative digit.as
#   Next: Ask for input if they enter something funky at the command line
#

# if len(sys.argv) > 1: check if length of input is

# Verify number is a valid non-negative integer
# def verify_number(user_input):
    #if user_input < 0:
'''
def verify_integer(is_int):
    try:
        make_int = int(is_int)
        return(make_int)

    except ValueError:
        print "Sorry, your input is invalid"
        return("A")

    else:
        print "Sorry, your input is invalid"
        return(4)
''''' \
''
user_input = sys.argv[1]
# get_number = verify_integer(user_input)

# while get_number == "A"\


user_input = input("Please input a valid non negative integer: ")
#get_number = verify_integer(user_input)
# Tried to create a function to verify the input is a number.
# Will have to come back some time.
#get_number = int(sys.argv[1])# Grab your argument
#if get_number == ""
   # print("This script requires a single non negative digit. Please try again")
    #exit()
#else

# if  is_int != int:
#    print("This script requires a single non negative digit. Please try again")
#    exit()
# need to add devinsive codin'''
'''
def do_fibbonacci(fib_input):
    fib_numbers = [0,1] # create a list
    for i in range(fib_input):
        fib_numbers.append(fib_numbers[i] + fib_numbers[i+1])
        return fib_numbers #print the list!
'''


fib_numbers = [0,1] # create a list
    # if get_number == 1:
    # return 1
    # else get_number == 0:
        #return 0

for i in range(get_number): #just learned range! It gives me all the numbers!
    # Grab the index i and the next index (i + 1) and add those beezys!
    fib_numbers.append(fib_numbers[i] + fib_numbers[i+1])
print fib_numbers #print the list!
