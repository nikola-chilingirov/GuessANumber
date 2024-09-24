import random
from colorama import Fore, Back, Style
flag = True
while flag:
    counter = 0
    next_level = False
    end = 100
    level = random.randint(1, end)
    range_lev = "1-100"
    while counter < 8:
        player_input = input(Fore.YELLOW + f"Guess the number with {8 - counter} attempts {range_lev}:")
        if not player_input.isdigit():
            print("Invalid input. Try again...")
            continue
        else:
            player_input_int = int(player_input)
        counter += 1
        if counter == 8 and player_input_int != level:
            print(f"You can`t guess the number with {counter} attempts")
            break
        if player_input_int == level:
            print(f"You guess with {counter} attempts!")
            next_level = True
            break
        elif player_input_int > level:
            print("Too High!")
        else:
            print("Too Low!")
    if next_level:
        counter = 0
        end += 100
        range_lev = "1-200"
        player_input = input(Fore.YELLOW + f"Next level or Exit: [Y] or [N]")
        if player_input == "Y":
            continue
        #else:
            #break
    else:
        restart = input("Play again [Y] or [N]: ")
        if restart == "Y":
            counter = 0
            flag = True
        else:
            break
