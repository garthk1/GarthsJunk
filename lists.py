
# Returns the factorial of the argument number. 
# number is actually a parameter. But the number that is returned, is the argument. 

def factorial(number):
    if number <= 1: #base case
        return 1
    else:
        return number * factorial(number-1)


user_input = input("Enter a non-negative integer to take the factorial of: ")
factorial_of_user_input = factorial(user_input)

print factorial_of_user_input