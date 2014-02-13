# Assignment 2: Write a Python script that generates the nth sequence
# of the Fibonacci numbers. The script will take exactly one command
# line argument for n.
# filename : fibonacci.py
# Author: Garth
import sys

get_number = int(sys.argv[1]) # Grab your argument


# need to add devinsive coding


fib_numbers = [0,1] # create a list
    if get_number == 1:

for i in range(get_number): #just learned range! It gives me all the numbers!
    # Grab the index i and the next index (i + 1) and add those beezys!
    fib_numbers.append(fib_numbers[i] + fib_numbers[i+1])
print fib_numbers #print the list!
