import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score,c_score):
    if u_score == c_score :
        print("Draw")
    elif u_score == 0:
        print("You win with a Black Jack!")
    elif c_score == 0:
        print("You lose ! Opponent have a Black Jack! ")
    elif u_score > 21:
        print("You went over! You Lose!")
    elif c_score > 21:
        print("You Win! Opponent went over")
    elif u_score > c_score:
        print("You Win!")
    else:
        print("You Lose!")

def want_to_play():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards are: {user_cards}, current score: {user_score} ")
        print(f"Computers first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal=input("Type 'y' to get another card, Type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final cards: {user_cards} , final score : {user_score} ")
    print(f"Computers final cards: {computer_cards} , final score: {computer_score}")
    compare(user_score,computer_score)


while input("Do you want to play a game of BlackJack? 'y' or 'n'") == "y":
    print("\n"*20)
    want_to_play()
