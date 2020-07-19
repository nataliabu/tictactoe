grid_content = list(range(1, 10))
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
            elif grid_content[choice-1] == choice:
                grid_content[choice-1] = "X"
            else:
                print("sorry baby, already taken")
                choice = None
