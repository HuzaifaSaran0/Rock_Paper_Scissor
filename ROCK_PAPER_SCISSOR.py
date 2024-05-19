import random


class bcolors:
    ENDC = '\033[0m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # Regular foreground colors
    BLACK = '\033[30m'
    REDD = '\033[31m'
    BLUEE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    # Regular background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Bright (bold) background colors
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'

    # Bright (bold) foreground colors
    BRIGHT_BLACK = '\033[30;1m'
    BRIGHT_RED = '\033[31;1m'
    BRIGHT_GREEN = '\033[32;1m'
    BRIGHT_YELLOW = '\033[33;1m'
    BRIGHT_BLUE = '\033[34;1m'
    BRIGHT_MAGENTA = '\033[35;1m'
    BRIGHT_CYAN = '\033[36;1m'
    BRIGHT_WHITE = '\033[37;1m'


choices = ["Rock", "Paper", "Scissor"]
enemy_score = 0
player_score = 0
draw = 0


def scores():
    pass
    # if player() == enemy():
    #     draw += 1
    # print(f"Draw:{draw} You Won:{player_score} Enemy won: {enemy_score}")
    # # pass


def choose():
    for choice in choices:
        if choice == choices[-1]:
            print(bcolors.BLUE + choice, end="\n" + bcolors.ENDC)
        else:
            print(bcolors.BLUE + choice, end="   " + bcolors.ENDC)


def player():
    choose()
    my_choice = input(bcolors.RED + bcolors.BOLD + "choose one:" + bcolors.ENDC)
    print(bcolors.PURPLE + bcolors.BOLD + f"You chose: {my_choice}" + bcolors.ENDC)
    return my_choice


def enemy():
    enemy_choice = random.choice(choices)
    print(bcolors.PURPLE + bcolors.BOLD + f"Enemy chose: {enemy_choice}\n" + bcolors.ENDC)
    return enemy_choice


i = 1


def RSP():
    global player_score, enemy_score, draw, i
    while i != 9:
        print(bcolors.BOLD + bcolors.YELLOW + f"Player score:{player_score}\nEnemy Score:"
                                              f"{enemy_score}\nDraw:{draw}" + bcolors.ENDC)
        player_choice = player()
        enemy_choice = enemy()
        i += 1
        if player_choice.title() == enemy_choice:
            print(bcolors.RESET + bcolors.BOLD + "Draw!!!\n" + bcolors.ENDC)
            draw += 1
        elif player_choice.upper() == "ROCK" and enemy_choice == "Scissor":
            player_score += 1
            print(bcolors.BG_CYAN + bcolors.BOLD + bcolors.RED + "Yeah!!You Got 1 Point.", bcolors.ENDC + "\n")
        elif player_choice.upper() == "ROCK" and enemy_choice == "Paper":
            enemy_score += 1
            print(bcolors.BG_CYAN + bcolors.BOLD + bcolors.RED + "Oops!!Enemy Got 1 Point.", bcolors.ENDC + "\n")
        elif player_choice.upper() == "SCISSOR" and enemy_choice == "Rock":
            enemy_score += 1
            print(bcolors.BG_CYAN + bcolors.BOLD + bcolors.RED + "Oops!!Enemy Got 1 Point.", bcolors.ENDC + "\n")
        elif player_choice.upper() == "SCISSOR" and enemy_choice == "Paper":
            player_score += 1
            print(bcolors.BG_CYAN + bcolors.BOLD + bcolors.RED + "Yeah!!You Got 1 Point.", bcolors.ENDC + "\n")
        elif player_choice.upper() == "PAPER" and enemy_choice == "Rock":
            player_score += 1
            print(bcolors.BG_CYAN + bcolors.BOLD + bcolors.RED + "Yeah!!You Got 1 Point.", bcolors.ENDC + "\n")
        elif player_choice.upper() == "PAPER" and enemy_choice == "Scissor":
            enemy_score += 1
            print(bcolors.BG_CYAN + bcolors.BOLD + bcolors.RED + "Oops!!Enemy Got 1 Point.", bcolors.ENDC + "\n")
        else:
            print(bcolors.BG_CYAN + bcolors.BOLD + bcolors.RED + "Invalid Input", bcolors.ENDC + "\n")
            i -= 1
        return player_score, enemy_score, draw


j = 1

while j <= 9:
    RSP()
    j += 1
print(bcolors.BOLD + bcolors.YELLOW + f"Player score:{player_score}\nEnemy Score:"
                                      f"{enemy_score}\nDraw:{draw}" + bcolors.ENDC)
if player_score > enemy_score:
    print(bcolors.MAGENTA + bcolors.BOLD + "\nHurry!!You Won the Game." + bcolors.ENDC)
elif player_score < enemy_score:
    print(bcolors.MAGENTA + bcolors.BOLD + "\nOops!!You Lost the Game." + bcolors.ENDC)
else:
    print(bcolors.MAGENTA + bcolors.BOLD + "\nlol!Match Drawn" + bcolors.ENDC)