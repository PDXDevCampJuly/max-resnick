# The amazing maze
from datetime import datetime


def valid(choice, doors):
    if choice.lower() in doors:
        return True


def prompt(doors, timeout=30):
    invalid = True
    while invalid:
        # Print Avail Doors
        print("Doors available in this room are:")
        for door in doors:
            print("\t- {}".format(door), sep="\n")
        start_time = datetime.now()
        choice = input("Which door would you like to use? ")
        end_time = datetime.now()
        # handle response
        elapsed_time = end_time - start_time
        if int(elapsed_time.total_seconds) > timeout:
            death(True)
        elif valid(choice, doors):
            invalid = False
            return choice.lower()
        else:
            print("An invalid choice was made. Please try again.")


def process_movement(description, doors):
    # print the desc of the room
    print(description)

    # Prompt for what they want
    choice = prompt(doors)

    # Get room
    doors[choice.lower()]()


def room0():
    description = "This is a room with table and small vile."
    doors = {"north": room1,
             "west": death,
             "south": room2}
    process_movement(description, doors)


def room1():
    description = "This room is lined with gold, and snake carvings."
    doors = {"west": death,
             "south": room0,
             "east": room4}
    process_movement(description, doors)


def room2():
    description = "This is very small room, that's very dry."
    doors = {"north": room0,
             "east": room3}
    process_movement(description, doors)


def room3():
    description = "This is a room is moderately sized with \
                   Black Betty playing on a loop at 93 Db SPL, \
                   quick get out."
    doors = {"north": room4,
             "east": death,
             "south": room1}
    process_movement(description, doors, 5)


def room4():
    description = "The walls are closing in on you, quick, pick a room."
    doors = {"north": room1,
             "west": leave,
             "south": room3}
    process_movement(description, doors, 10)


def death(timeout=False):
    if not timeout:
        description = """
        Congrats, you just walked into an empty pit with spikes
        you've fallen on many many spikes and have died.
        wwwwwwwomp....
        """
    elif timeout:
        description = """
        Oh no you took to long and the room killed you.
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
    print("Welcome to the Alice in Wonderland Maze!")
    room0()
