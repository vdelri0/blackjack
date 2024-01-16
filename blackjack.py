############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import os
from art import logo
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return a score."""
    if len(cards) == 2:
        if sum(cards) == 21:
            return 0 # blackjack
        else:
            return sum(cards)
    else:
        score = sum(cards)
        if score > 21 and 11 in cards: # ace condition
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
        return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "¡Draw!"
    elif computer_score == 0:
        return "¡Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "¡Win with a Blackjack!"
    elif computer_score > 21:
        return "¡Opponent went over. You win!"
    elif user_score > 21:
        return "¡You went over. You lose!"
    elif user_score > computer_score:
        return "¡You win!"
    else:
        return "¡You lose!"

def play_blackjack():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards: {user_cards}, current score: {user_score}\n")
        print(f"computer's first card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: \n")
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}\n")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}\n")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': \n") == "y":
    cls()
    play_blackjack()