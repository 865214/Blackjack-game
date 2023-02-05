############### Blackjack Project #####################

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
from replit import clear
from art import logo
import random
# Step 1: For starting our game we create a variable called start_a_game if the user press 'y' it will clear out our console and start our game and also prints our logo
start_a_game = input("Do you want to play a game of Black Jack? Type 'y' or 'n'\n").lower()
if start_a_game == 'y':
  clear()
  print(logo)


def blackjack():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Step 2 : Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
# The deal_card() random select number from the list
  def deal_card(card):
    random_card = random.choice(card)
    return random_card
  # Step 3: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  user_cards.append(deal_card(cards))
  user_cards.append(deal_card(cards))
  user = user_cards
  computer_cards.append(deal_card(cards))
  computer = computer_cards
  # Another way to append 2 cards in a list using for_loops
  # for _ in range(2):
  #   user_cards.append(deal_card(cards))
  #   computer_cards.append(deal_cards(cards))

#Step 4: create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

  def calculate_score(cards):
    user_sum = sum(cards)
    # Step 5: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return ) 0 
    #instead of the actual score. 0 will represent a blackjack in our game.
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace 
    # it with a 1. You might need to look up append() and remove().
    if 11 in cards and user_sum > 21:
      cards.remove(11)
      cards.append(1) 
    return user_sum
  # Step 6 : Create a function called computer_draw() so that computer also drawing the card at the same time while user drawing cards 
  def computer_draw():
    while calculate_score(computer)<17:
      computer.append(deal_card(cards))
    print(f"Computer Final hand:{computer},Final_score{calculate_score(computer)}")
  
  # Step 7: Create a function called compare() which will try to compare the scores of user score as well as the computer score
  def compare():
    if calculate_score(user) == 21:
      print("It's a Blackjack for You. You win")
    elif calculate_score(computer) == 21:
      print("It's a blackjack for Opponent.You lose")
    elif calculate_score(user)>21:
      print('You went over Opponent. You lose')
    elif calculate_score(computer)>21:
      print("Opponent went over. You win")
    elif calculate_score(user) > calculate_score(computer):
      print("You have an upper hand. You win")
    elif calculate_score(user) < calculate_score(computer):
      print("Oppenent has an upper hand. You lose")
    elif calculate_score(user) == calculate_score(computer):
      print("Draw")
  # Step 8 : we are creating an while loop so that everytime user ask to draw another card it will show us the score user and after comparing the score of user as well as computer we are deciding who is wining and who is losing.
  game_ends = True
  while game_ends:
    print(f"Your cards:{user},Current Score:{calculate_score(user)}")
    print(f"Computer first Card: {computer[0]}")
    if calculate_score(user) == 21 or calculate_score(computer) == 21:
      game_ends = False
      print(f"Your Final Hand:{user},Final_Score:{calculate_score(user)}")
      computer_draw()
      compare()
    elif calculate_score(user) > 21:
      game_ends = False
      print(f"Your Final Hand:{user},Final_Score:{calculate_score(user)}")
      computer_draw()
      compare()
    elif calculate_score(user) < 21:
      game_ends = True
      user_draw = input("Draw another card? Type 'y' to draw and type 'n' to exit\n").lower()
      if user_draw == 'y':
        user.append(deal_card(cards))
        game_ends = True
        if sum(user) > 21:
          game_ends = False
          print(f"Your Final Hand:{user},Final_Score:{calculate_score(user)}")
          computer_draw()
          compare()
        elif sum(user)<21:
          game_ends = True
        elif sum(user) == 21:
          game_ends = False
          print(f"Your Final Hand:{user},Final_Score:{calculate_score(user)}")
          computer_draw()
          compare()
      elif user_draw == 'n':
        game_ends = False
        print(f"Your Final Hand:{user},Final_Score:{calculate_score(user)}")
        computer_draw()
        compare()
    
blackjack()
#step 9 : At the end we are creating an function blackjack() to summarize all our code so that everytime time we call that function it will start our game

#Step 10 : We are using while loop again because if the wanted to restart the game again then it will say 'y' then automatically clears out our previous game and starting  new game again without hitting the 'run' button again.
while input("Type y to play again blackjack game and Type 'n' to exit\n") == 'y':
  clear()
  print(logo)
  blackjack()
