import random
from colorama import Fore, Back, Style
target = random.randint(1, 100)
while True:
    player_input = input(Fore.YELLOW + "Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    else:
        player_input_int = int(player_input)
    if player_input_int == target:
        print("You guess it!")
        break
    elif player_input_int > target:
        print("Too High!")
    else:
        print("Too Low!")