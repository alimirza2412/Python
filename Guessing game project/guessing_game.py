import random

easy_words = ["Cat", "Dog", "Sad", "Fast", "Clean", "see", "Eye", "Bed"]

medium_words = [ "Apple", "Train", "Money", "Sindh", "Tiger", "Liger", "Mouse", "Hand"]

hard_words = ["Elephant", "Diamond", "Computer", "Laptop", "System", "Windows", "Mountain"]

print("WELCOME TO RANDOM GUESSING GAME 🤗")

print("Choose the difficulty level: Easy, Medium, Hard")

level = input("Enter difficulty level : ").lower()

if level == "easy":
    choose = random.choice(easy_words).lower()
elif level == "medium":
    choose = random.choice(medium_words).lower()
elif level == "hard":
    choose = random.choice(hard_words).lower()
else:
    print("Default to easy level: This level is not present Here 😢 ")
    choose = random.choice(easy_words).lower()

attempt = 0

print("\nGuess the secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempt += 1

    if guess == choose:
        print(f"CONGRATS! You guessed it in {attempt} attempts")
        break

    hint = ""

    for i in range(len(choose)):
        if i < len(guess) and guess[i] == choose[i]:
            hint += guess[i]

        else:
              hint += "_"

    print("Hint: ", hint)

print("Game Over")