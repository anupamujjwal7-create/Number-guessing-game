import random

lower_bound = 1
upper_bound = 100
max_attempts = 7

print("Welcome to the Number Guessing Game!")

while True:  # Outer loop to keep the game running again and again
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    print(f"\nGuess a number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
            
        attempts += 1
        
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry! You've used all attempts. The number was {secret_number}.")
        
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ('yes', 'y'):
        print("Thanks for playing! Goodbye!")
        break  # Exits the outer while True loop and ends the program