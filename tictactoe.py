print("   |   |   \n---+---+---\n   |   |   \n---+---+---\n   |   |   ")
choice = None
while choice is None:
    try:
        choice = int(input("Where do you want to play: "))
    except ValueError:
        choice = None
print(type(choice))
