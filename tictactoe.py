import time

grid_content = list(range(1, 10))
turn_count = 0
current_player = 0
players_attributes = [
    {"name": "", "character": "X", "type": ""},
    {"name": "", "character": "O", "type": ""}
]

winning_cases = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),

    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),

    (0, 4, 8),
    (2, 4, 6)
)

def render(grid):
    def element_color(element):
        try:
            return "\033[38;5;246m{}\033[0m".format(int(element))
        except ValueError:
            return "\033[38;5;123m{}\033[0m".format(element)

    print("\033[2J\033[0;0H") # clear the screen and move cursor at the top
    print(" {} | {} | {} ".format(*[element_color(element) for element in grid[:3]]))
    print("---+---+---")
    print(" {} | {} | {} ".format(*[element_color(element) for element in grid[3:6]]))
    print("---+---+---")
    print(" {} | {} | {} ".format(*[element_color(element) for element in grid[6:]]))


def get_winning_choice(player):
    choice = None
    for case in winning_cases:
        potential_choice = None
        count_win_cases = 0
        for index in case:
            item = grid_content[index]
            if item == players_attributes[player]["character"]:
                count_win_cases += 1
            elif item == index + 1:
                potential_choice = item
        if count_win_cases == 2 and potential_choice is not None:
            choice = potential_choice
            break
    return choice


print("\033[2J\033[0;0H") # clear the screen and move cursor at the top

number_of_players = None
while number_of_players is None:
    number_of_players = input("Number of players (1 or 2): ")
    if number_of_players not in {"1", "2"}:
        print("You have to type an integer between 1 and 2")
        number_of_players = None

players_attributes[0]["type"] = "human"
if number_of_players == "2":
    players_attributes[0]["name"] = input("What is your name player 1: ")
    players_attributes[1]["name"] = input("What is your name player 2: ")
    players_attributes[1]["type"] = "human"
else:
    players_attributes[0]["name"] = input("What is your name: ")
    players_attributes[1]["type"] = "machine"

render(grid_content)
while True:
    if players_attributes[current_player]["type"] == "human":
        choice = None
        while choice is None:
            choice = input("{}, where do you want to play (1 to 9): ".format(players_attributes[current_player]["name"]))
            try:
                choice = int(choice)
            except ValueError:
                print("You have to type an integer between 1 and 9")
                choice = None
            else:
                if not(1 <= choice <= 9):
                    print("You have to type an integer between 1 and 9")
                    choice = None
                elif grid_content[choice-1] != choice:
                    print("Sorry baby, already taken")
                    choice = None
    else:
        choice = get_winning_choice(current_player)
        if choice is None:
            choice = get_winning_choice((current_player + 1) % 2)
            if choice is None:
                places_priority = (5, 1, 3, 7, 9, 2, 4, 6, 8)
                for place in places_priority:
                    if grid_content[place-1] == place:
                        choice = place
                        break
        print("The computer is playing in {}".format(choice))
        time.sleep(2)

    grid_content[choice-1] = players_attributes[current_player]["character"]

    render(grid_content)

    turn_count += 1

    if (grid_content[0] == grid_content[1] and grid_content[1] == grid_content[2]
        or grid_content[3] == grid_content[4] and grid_content[4] == grid_content[5]
        or grid_content[6] == grid_content[7] and grid_content[7] == grid_content[8]
        or grid_content[0] == grid_content[3] and grid_content[3] == grid_content[6]
        or grid_content[1] == grid_content[4] and grid_content[4] == grid_content[7]
        or grid_content[2] == grid_content[5] and grid_content[5] == grid_content[8]
        or grid_content[0] == grid_content[4] and grid_content[4] == grid_content[8]
        or grid_content[2] == grid_content[4] and grid_content[4] == grid_content[6]
    ):
        if players_attributes[current_player]["type"] == "human":
            print("Congrats {}, you won".format(players_attributes[current_player]["name"]))
        else:
            print("The computer won :-( ... this time")
        break
    elif turn_count == 9:
        print("\033[38;5;212m")
        print(" _")
        print("/ \\")
        print("\\ /")
        print(" o")
        print("/ \\")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("\\./")
        print("\033[0m")
        print("It's a tie")
        print("")
        break

    current_player = (current_player + 1) % 2
