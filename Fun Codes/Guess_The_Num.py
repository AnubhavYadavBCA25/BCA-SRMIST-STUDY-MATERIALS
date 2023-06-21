print("Welcome To Guess The Number Game!\n")

import random
actual_number = int(random.randint(1, 30))


moves_take = 1
while moves_take < 6:
    try:
        guess_number = int(input("Guess A Number Between 1 to 30: "))
    except ValueError:
        print("Invalid Input. Please Enter A Number.")
        continue

    if guess_number < actual_number:
        print("Your Guess Is Too Low.")
    elif guess_number > actual_number:
        print("Your Guess Is Too High.")
    else:
        print("Congratulation you guessed the correct number in {} guesses.".format(moves_take))
        break

    moves_take += 1
    
    if moves_take == 6:
        print("\nSorry, You Lose. The Number Was",actual_number)
        play_again = input("Do You Want To Play Again? (yes/no): ")
        if play_again == 'yes':
            moves_take = 1
            actual_number = int(random.randint(1, 20))
        else:
            break

print("\nThank You For Playing :)")


