print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")
choice = None
while choice is None:
    try:
        choice = int(input("Where do you want to play: "))
    except ValueError:
        choice = None
print(type(choice))
