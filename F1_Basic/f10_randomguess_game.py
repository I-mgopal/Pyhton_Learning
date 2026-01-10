import random
# Generate random number bte 1-10
num = random.randint(1,11)
count = 0

while True:
    # Guess the number
    guess_num = int(input("Enter the number btw (1 - 10):- "))
    count = count + 1

    #Check the guess number is same or not
    if(guess_num == num):
        print(f"You guess the right number with {count} count, and number is {num}")
        break
    elif num>guess_num:
        print(f"Guess number is wrong, Choose little higher{chr(128522)}")
    else:
        print(f"Guess number is wrong, Choose little lower{chr(128522)}")
