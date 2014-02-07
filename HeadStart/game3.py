from random import randint
secret = randint(1,20)
count = 6
print("Welcome!")


while count != 0:
    print("You have", count, "more tries")
    g = input("Guess the number: ")
    guess = int(g)
    count = count - 1

    if guess == secret:
        print("You win!")

    else:
        if guess > secret:
            print("Too high!")

        else:
            print("Too low!")

print("Game over!")
