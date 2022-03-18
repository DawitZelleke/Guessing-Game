import random

def main():
    numOfGuesses = 0    
    run = True
    quit = False
    print("Hello! Welcome to the number guessing game!")
    user = input("What is your name: ")
    while True:
        user = input(f"Okay {user}! Starting at 1, what is the max range you'd like to guess from? ")
        if user.isdigit():
            break
        print("Invalid input")
    randomNumber = random.randint(1,int(user))
    print(randomNumber)
    print(f"Gotcha! I am guessing a number between 1 and {user}")
    while run and not quit:
        user_input = input("Guess or -1 to quit: ")
        if user_input == "-1":
            quit = True
        elif user_input.isdigit() and int(user_input) > 0:
            if int(user_input) < randomNumber:
                print("Your Guess was lower")
            elif int(user_input) > randomNumber:
                print("Your guess was higher")
            else:
                print("YAY! YOU GOT IT")
                run = False
            numOfGuesses += 1
        else:
            print("Invalid input")
    
    print("Thanks for playing!")
    if not run:
        print(f"You guessed the number in {numOfGuesses} tries!")

main()