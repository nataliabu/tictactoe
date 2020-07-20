grid_content = list(range(1, 10))
current_player = 0
players = ("X", "O")
while True:
    print(" {} | {} | {} ".format(*grid_content[:3]))
    print("---+---+---")
    print(" {} | {} | {} ".format(*grid_content[3:6]))
    print("---+---+---")
    print(" {} | {} | {} ".format(*grid_content[6:]))

    choice = None
    while choice is None:
        choice = input("Where do you want to play: ")
        try:
            choice = int(choice)
        except ValueError:
            choice = None
        else:
            if not(1 <= choice <= 9):
                choice = None
            elif grid_content[choice-1] != choice:
                print("sorry baby, already taken")
                choice = None

    grid_content[choice-1] = players[current_player]

    if (grid_content[0] == grid_content[1] and grid_content[1] == grid_content[2]
        or grid_content[3] == grid_content[4] and grid_content[4] == grid_content[5]
        or grid_content[6] == grid_content[7] and grid_content[7] == grid_content[8]
        or grid_content[0] == grid_content[3] and grid_content[3] == grid_content[6]
        or grid_content[1] == grid_content[4] and grid_content[4] == grid_content[7]
        or grid_content[2] == grid_content[5] and grid_content[5] == grid_content[8]
        or grid_content[0] == grid_content[4] and grid_content[4] == grid_content[8]
        or grid_content[2] == grid_content[4] and grid_content[4] == grid_content[6]
    ):
        print("Congrats player {}, you won".format(players[current_player]))

    current_player = (current_player + 1) % 2
