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


get_input = sys.argv

how_many = len(get_input)
print how_many

if how_many != 2:
    user_input = raw_input("Invalid input. Please enter a single non negative integer only: ")
else:
    user_input = get_input[1]

is_digit = user_input.isdigit()

while is_digit == False:
    user_input = raw_input("Invalid input. Please enter a single non negative integer only: ")
    is_digit = user_input.isdigit()

get_number = int(user_input)
''' This may not be needed!
if get_number == 1:
    print"[0, 1]"
    exit()
elif get_number == 0:
    print "[0]"
    exit()
else:
'''

fib_numbers = [0,1] # create a list

for i in range(get_number): #just learned range! It gives me all the numbers!
    # Grab the index i and the next index (i + 1) and add those beezys!
    fib_numbers.append(fib_numbers[i] + fib_numbers[i+1])
print fib_numbers[0:get_number+1] #print the list!
