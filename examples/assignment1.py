"""
Desired outcome:
What is your name?
> Bob
Do you want to go to the mall or the beach?
> mall
Bob, you are at the mall.


OR


What is your name?
> Alice
Do you want to go to the mall or the beach?
> beach
Alice, you are at the beach. 
"""

def get_player_name():
  # TODO: Use the input() function to get the player's name
  name = input("What is your name?")

def get_initial_choice():
  # TODO: Ask the player if they want to go to the mall or the beach
  pass

def print_message(name, location):
  # TODO: Print the message "name, you are at the location."
  pass

def main():
  player_name = get_player_name()
  player_choice = get_player_choice()
  print_message(player_name, player_choice)

if __name__ == "__main__":
  main()

