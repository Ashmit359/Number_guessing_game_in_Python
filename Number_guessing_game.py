import random

print("Welcome to the number guessing game! You have 7 chances to guess the number.")

number_to_guess = random.randint(0, 100)

for guess_counter in range(1, 8):
    my_guess = int(input('Enter your guess: '))

    if my_guess == number_to_guess:
        print(f'Congrats! The number is {number_to_guess}, found it in {guess_counter} attempts.')
        break
    elif my_guess > number_to_guess:
        print('Your guess is too high.')
    else:
        print('Your guess is too low.')

if my_guess != number_to_guess:
    print(f'Sorry, the number was {number_to_guess}. Better luck next time!')
