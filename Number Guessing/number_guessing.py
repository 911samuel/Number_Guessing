import random

top_range = input("Enter the maximum number: ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_range)
guesses = 0
max_guesses = 5  # You can change this value to limit the number of guesses
remaining_guesses = max_guesses

while True:
    guesses += 1
    remaining_guesses -= 1
    guess_number = input("Make a guess: ")

    if guess_number.isdigit():
        guess_number = int(guess_number)
        if guess_number < 0 or guess_number > top_range:
            print("Your guess should be between 0 and", top_range)
            continue
    else:
        print("Please type a number next time.")
        continue

    if guess_number == random_number:
        print("You got it!")
        break
    elif guess_number > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

    if remaining_guesses == 0:
        print("You have used all your guesses. The number was", random_number)
        break

    print("Remaining guesses:", remaining_guesses)

play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
    random_number = random.randint(0, top_range)
    guesses = 0
    remaining_guesses = max_guesses
    print("New game started! You have", max_guesses, "guesses.")
else:
    print("Thanks for playing!")
