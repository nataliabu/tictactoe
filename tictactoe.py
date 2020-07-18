while True:
    print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")
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
