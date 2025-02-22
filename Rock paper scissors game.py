rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
import random
comp_choice = random.choice(choices)


if user_choice == 0:
    print(rock)
    print(f"computer choice: \n {comp_choice}")
    if comp_choice == rock:
        print("Its a draw")
    elif comp_choice == paper:
        print("You lose")
    elif comp_choice == scissors:
        print("You win")
    else:
        print("Wrong Input")
elif user_choice == 1:
    print(paper)
    print(f"computer choice: \n {comp_choice}")
    if comp_choice == rock:
        print("You win")
    elif comp_choice == paper:
        print("Its a draw")
    elif comp_choice == scissors:
        print("You lose")
    else:
        print("Wrong Input")
elif user_choice == 2:
    print(scissors)
    print(f"computer choice: \n {comp_choice}")
    if comp_choice == rock:
        print("You lose")
    elif comp_choice == paper:
        print("You win")
    elif comp_choice == scissors:
        print("Its a draw")
    else:
        print("Wrong Input")
else:
    print("Wrong Input1")
