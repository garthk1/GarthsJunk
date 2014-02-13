'''
nth_number = sys.argv[1]
int(nth_number)
fib_first = 0
fib_second = 1
while fib_first <= nth_number:
    print fib_first
    fib_first = fib_second
    fib_second = fib_first + fib_second
'''

'''
def fibonacci(fib_num):
    first_num = -1
    next_num = 1
    i = 0
    while i <= fib_num:
        sum = first_num + next_num
        first_num = next_num
        next_num = sum
        i += 1
        return next_num

get_final = input("How far would you like to go?: ")
fib_sequence_activate = fibonacci(get_final)
print fib_sequence_activate
'''