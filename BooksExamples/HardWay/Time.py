__author__ = 'gkline'

time_now = int(input("What time is it?"))
time_wait = int(input("How long should I wait?"))

hours = time_now + time_wait

time_of_day = hours % 24

print("Your alarm will go off at", time_of_day)
