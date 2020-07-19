grid_content = list(range(1, 10))
while True:
    print(" {} | {} | {} \n---+---+---\n {} | {} | {} \n---+---+---\n {} | {} | {} ".format(*grid_content))
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
    print(type(choice))
