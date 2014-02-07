from random import randint
secret = randint(1,20)
guess = 0
print("Welcome!")

while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)

    if guess == secret:
        print("You win!")
    else:
        if guess > secret:
            print("Too high!")

        else:
            print("Too low!")

print("Game over!")
