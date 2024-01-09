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

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

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

def max_score(user_score, computer_score):
    if user_score == computer_score:
        print("Push!")
    else:
        max_score = max(user_score, computer_score)
        if user_score == max_score:
            print("¡You Win!\n")
        else:
            print("Game Over\n")
    return True

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

    if (user_score or computer_score) == 0:
        print("¡Black Jack!")
        end = max_score(user_score, computer_score)
    elif (user_score or computer_score) > 21:
        end = max_score(user_score, computer_score)
    else:
        another = input("Type 'y' to get another card, type 'n' to pass: \n")
        if another == "y":
            user_cards.append(deal_card())
            continue
        else:
            end = True

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.