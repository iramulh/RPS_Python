my_wins = 0
bot_wins = 0
ties = 0
game_over = False

def play_rps():
  """Simulates one round of rock-paper-scissors.
  
  First, it prompts the user to enter "rock", "paper", or "scissors". If the user enters "quit", the game ends (game_over becomes True). If the user enters anything else, it prompts them again. 
  
  If the user didn't quit, the bot is assigned "rock", "paper", or "scissors" at random.

  Then, it displays the user's move and the bot's move and says who won the round. The three global variables that keep track of the score are updated.
  """
  #specifies that the variables are global and not local
  global my_wins
  global bot_wins
  global ties
  global game_over

  #importing the random library because it will be used to selct the bot's move
  import random
  
  while True:

    #possible moves for the bot to picks and also to compare the user's move with
    moves = ["rock", "paper", "scissors"]

    #picks the bot's move randomly
    bot_move = random.choice(moves)

    #promt the user to make their move
    user_move = input("Enter \'rock\', \'paper\', or \'scissors\': ")

    #makes it lowercase no matter how the user inputs it so that less problems occur
    user_move = user_move.lower()

    #sees if their move is valid
    if user_move in moves:

      #prints their move as well as the bots
      print("You chose "+ user_move)
      print("Bot chose "+ bot_move)

      #for a tie when the user's move is the same as the bot's
      if user_move == bot_move:
        print("It's a tie!")
        ties += 1
        break

      #for win cases if they beat the bot
      elif user_move + bot_move == "rockscissors" or user_move + bot_move == "paperrock" or user_move + bot_move == "scissorspaper":
        print("You win!")
        my_wins += 1
        break

      #for loss cases when the bot wins
      elif bot_move + user_move == "rockscissors" or bot_move + user_move == "paperrock" or bot_move + user_move == "scissorspaper":
        print("Bot win!")
        bot_wins += 1
        break

    #if they decide to quit then it sets game_over to true so that the program stops running
    elif user_move == "quit":
      print("Okay, bye.")
      game_over = True
      break
      
    else:
      pass
    


def display_score():
  """Displays the score in the following format:
  My wins: _
  Bot's wins: _
  Ties: _
  """

  #modifying the scope to use the necessary global variables in the function instead of creating local ones
  global my_wins
  global bot_wins
  global ties

  #prints the status of the scores
  print("My wins: " + str(my_wins))
  print("Bot's wins: " + str(bot_wins))
  print("Ties: " + str(ties))
  
  # What goes here?
  pass # Delete this line when you're done

# Don't modify anything below here
while not game_over:
  display_score()
  play_rps()
  