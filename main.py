import math
import random

def calculator(operator, num1, num2):
    if operator == 1:
        answer = print(num1, "+", num2, "=", num1 + num2)
    elif operator == 2:
        answer = print(num1, "-", num2, "=", num1-num2)
    elif operator == 3:
        answer = print(num1, "*", num2, "=", num1*num2)
    elif operator == 4:
        answer = (num1/num2)
        formatAnswer = format(answer, ".2f")
        print(num1, "/", num2, "=", formatAnswer)
    elif operator == 5:
        answer = print(num1, "^", num2, "=", num1**num2)

    return answer

# Found help for heads or tails here: https://www.youtube.com/watch?v=ef6GuRfoSyo&t=191s

def decider(flips):
    import time
    for i in range(flips):
        winner = random.randint(0, 1)
        time.sleep(1)
        if winner == 0:
            print("Heads")
        else:
            print("Tails")
    
    return winner

# Found help with number game here: https://www.youtube.com/watch?v=ZsRMQHbx6Xc

def numberGame():
    number = random.randint(0, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    while guess != number:
        if guess > number:
            guess = int(input("Guess lower. Try again: "))
        else:
            guess = int(input("Guess higher. Try again: "))
    print("You got it! Good Job!")

# I got help with creating a right triangle shape here: https://www.youtube.com/watch?v=0PkIvXfP3ew&t=505s

def shapeMaker():
    shape = int(input("What shape would you like for me to make?\n1. SQUARE\n2. TRIANGLE\n3. RIGHT TRIANGLE\n"))
    if shape == 1:
        rows = int(input("Enter how many rows you would like: "))
        for row in range(rows):
            for column in range(rows):
                print("*", end=" ")
            print()
    elif shape == 2:
        rows = int(input("Enter how many rows you would like: "))
        for row in range(0, rows):
            for column in range(0, rows - row - 1):
                print(end=" ")
            for column in range(0, row + 1):
                print("*", end=" ")
            print()
    elif shape == 3:
        rows = int(input("Enter how many rows you would like: "))
        for row in range(1, rows + 1):
            print("* " * row)
    else:
        print("Since you decided to not follow the rules I am sending you back.")

def mycal():
    import calendar

    choice = int(input("Would you like to either see a specific month or entire year?"
                       "\n1.MONTH\n2.ENTIRE YEAR\n"))
    if choice == 1:
        year = int(input("Enter your desired year: "))
        month = int(input("Enter your desired month (1-12): "))
        calendar.setfirstweekday(calendar.SUNDAY)
        cal = calendar.month(year, month)
        print(str(cal))
    if choice == 2:
        year = int(input("Enter your desired year: "))
        calendar.setfirstweekday(calendar.SUNDAY)
        entcal = calendar.calendar(year)
        print(entcal)

def main():
    import time
    print("Hello, I am Rob.")
    time.sleep(1)
    print("Apologies, I am an early model so I do not have many functions at the moment.")
    time.sleep(1)
    option = int(input("How may I help you today? (Select a number)\n1. CALCULATOR\n2. HEADS OR TAILS\n"
                       "3. GUESS NUMBER GAME\n4. SHAPE MAKER\n5. CALENDAR\n6. STORY\n"))
    if option == 1:
        operator = int(input("Select operator:\n1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE\n"
                                "5. SQUARE\n"))
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        outcome = calculator(operator, num1, num2)
    elif option == 2:
        tosses = int(input("How many times would you like to roll? : "))
        getWinner = decider(tosses)
    elif option == 3:
        game = numberGame()
    elif option == 4:
        shapeMakerGame = shapeMaker()
    elif option == 5:
        calendar = mycal()
#Found story on https://www.pinterest.com/pin/453315518736832933/
    elif option == 6:
        print("Hello, welcome. First, you will name your two animals, then I will tell you a story.")
        hero = input("Enter the name of the smaller animal: ")
        villain = input("Enter the name of the larger animal: ")

        print("\nOnce upon a time, a", hero, "got too close to a", villain + ". The", villain, "started eating the",
              hero,
              '"Spare me!"\nthe', hero, 'cried. "And I will repay you in the future." The', villain, "let the",
              hero, "go"
                    ", although wondering how they can repay them.\nOne day the",
              villain, "got caught in a hunter's trap. The",
              villain, "cried for help, then the", hero, "came to the rescue.\nReleasing the", villain,
              "from the trap."
              " Then the", hero, "and the", villain, "became best friends.\n")
    time.sleep(1)
    restart = int(input("Would you like to restart?\n1. Yes\n2. No\n"))
    if restart == 1:
        main()
    elif restart == 2 and restart <= 2:
        print("Thank you for letting me assist you.")
        print("Have a great day.")
        print("Goodbye.")

main()