# The amazing maze

def start():
    print("Welcome to the Alice in Wonderland Maze!")
    room0()

def valid(choice, doors):
    if choice in doors:
        return True
    if choice not in doors:
        print("Careful, we're case sensitive.")


def prompt(doors):
    invalid = True

    while invalid:
        # Print Avail Doors
        print("Doors available in this room are:")
        for door in doors:
            print("\t- {}".format(door), sep="\n")
        choice = input("Which door would you like to use? ")
        # handle response
        if valid(choice, doors):
            invalid = False
            return choice
        else:
            print("An invalid choice was made. Please try again.")


def process_movement(description, doors):
    # print the desc of the room
    print(description)

    # Prompt for what they want
    choice = prompt(doors)

    # Get room
    doors[choice]()

def room0():
    description = "This is a room with table and small vile."
    doors = {"North":room1,
             "West":fall,
             "South":room2}
    process_movement(description, doors)


def room1():
    description = "This room is lined with gold, and snake carvings."
    doors = {"West":fall,
             "South":room0,
             "East":room4}
    process_movement(description, doors)


def room2():
    description = "This is very small room, that's very dry."
    doors = {"North":room0,
             "East":room3}
    process_movement(description, doors)


def room3():
    description = "This is a room is moderately sized with \
                   Black Betty playing on a loop at 93 Db SPL, \
                   quick get out."
    doors = {"North":room4,
             "East":fall,
             "South":room1}
    process_movement(description, doors)


def room4():
    description = "The walls are closing in on you, quick, pick a room."
    doors = {"North":room1,
             "West":leave,
             "South":room3}
    process_movement(description, doors)


def fall():
    description = """
    Congrats, you just walked into an empty pit with spikes
    you've fallen on many many spikes and have died.
    wwwwwwwomp....
    """
    print(description)
    exit()

def leave():
    description = """
    Congrats, you've escaped the evil crutches of the queen of
    spades. You've won.
    """
    print(description)
    exit()

if __name__ == '__main__':
    start()
