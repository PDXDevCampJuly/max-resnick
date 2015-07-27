# Madlib program via Python3 Day 1 of bootcamp


# Get first lib
lib = input("Who is this going to be about? ")

fullstory = lib + " has joined the search for "

# get 2nd lib
lib = input("How many are missing? ")
fullstory += lib + "teenage boys who disappeared"

# get 3rd lib
lib = input("where did they disappear from? ")
fullstory += " off the coast of " + lib + "during a fishing trip Friday, adding the USS "

# get 4th lib
lib = input("What's the name of the boat? ")
fullstory += lib + "to a Coast Guard search team that has covered about "
howfar = str(len(lib) * 20000)

fullstory += howfar + " square nautical miles — by air and sea — in the hunt for Austin Stephanos and Perry Cohen."

print(fullstory)
