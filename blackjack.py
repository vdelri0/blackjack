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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    choice = random.choice(cards)
    return choice

def calculate_score(cards):
    if len(cards) == 2:
        if (11 and 10) in cards:
            return 0 # blackjack
        else:
            return sum(cards)
    else:
        score = sum(cards)
        if score > 21: # ace condition
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
        return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Draw!")
    elif computer_score == 0:
        print("¡Black Jack!")
        print("Computer Wins!")
    elif user_score == 0:
        print("¡Black Jack!")
        print("User Wins!")
    elif computer_score > 21:
        print("User Wins!")
    elif user_score > 21:
        print("Computer Wins!")
    else:
        max_score = max(user_score, computer_score)
        if user_score == max_score:
            print("¡You Win!\n")
        else:
            print("Game Over\n")
    return True

def play_blackjack():
    end = False
    while not end:
        if not (user_cards and computer_cards):
            print(logo)
            for _ in range(0,2):
                user_cards.append(deal_card())
                computer_cards.append(deal_card())

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}\n")
        print(f"computer's first card: {computer_cards[0]}\n")

        another = input("Type 'y' to get another card, type 'n' to pass: \n")
        if another == "y":
            user_cards.append(deal_card())
            continue
        else:
            while computer_score < 17:
                computer_cards.append(deal_card())
            print(f"Computer's Cards: {computer_cards}, current score: {computer_score}\n")
            compare(user_score, computer_score)

        restart = input("Type 'y' if you want to restart, type 'n' to pass: \n")
        if restart == "y":
            cls()
            play_blackjack()
        else:
            end = True
