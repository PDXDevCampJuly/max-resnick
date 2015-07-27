# Madlib program via Python3 Day 1 of bootcamp

def get_input(question):
    return input(question)

def add_to_story(lib):
    # this is probably ugly :-)
    global the_full_monty
    the_full_monty += lib

the_full_monty = "\n\n"
fullstory = add_to_story(get_input("Who is this going to be about? "))
fullstory = add_to_story(" has joined the search for ")

# get 2nd lib
add_to_story(get_input("How many are missing? "))
add_to_story(" teenage boys who disappeared ")
add_to_story(" off the coast of ")
add_to_story(get_input("What coast are they off of? "))
add_to_story(" during a fishing trip Friday adding the USS ")

# we're gonna use boat_name to determine the size of the area.
boat_name = get_input("What's the name of the boat? ")
add_to_story(boat_name)
add_to_story(" to a Coast Guard search team that has covered about ")

# use boat name to determine our search area.
add_to_story(str(len(boat_name) * 20000))
add_to_story(" square nautical miles — by air and sea — in the hunt for Austin Stephanos and Perry Cohen.")

add_to_story("\n\n")
print(the_full_monty)
