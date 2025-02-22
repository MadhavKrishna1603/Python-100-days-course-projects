import random
print("Welcome to the number guessing Game!")
print("\n")
numbers = []
for i in range(0,101):
    numbers.append(i)
rand_num = random.choice(numbers)
print("I am thinking of a number between 1 and 100")
print("\n")
game_over = False
difficulty=input("Choose a dificulty. 'Easy' or 'Hard' :").lower()
print("\n")
attempts = 0
if difficulty == "easy":
    attempts = 10
    
elif difficulty == "hard":
    attempts = 5
    
while not game_over == True:
    print(f"You have {attempts} attempts to guess the number")
    guess = int(input("Guess a number: "))
    if attempts == 0:
        print("You have run out of guesses! Refresh the page and try again")
        game_over = True
    elif guess > rand_num:
        print("Too high!")
        print("Guess Again")
        print("\n")
        attempts -= 1
    elif guess < rand_num:
        print("Too low!")
        print("Guess Again")
        print("\n")
        attempts -= 1
    elif attempts == 0:
        print("You have run out of guesses! Refresh the page and try again")
        game_over = True
    elif guess == rand_num:
        print(f"You got it! The answer was {rand_num}")
        game_over = True
