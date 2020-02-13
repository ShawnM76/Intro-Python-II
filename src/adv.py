from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Create player
player_name = input("Whats your name?: ")

player = Player(player_name, room['outside'])  # keep track of player room

# user = input(
#     f"{player_name} welcome to the Adventure Game! Press any key to continue!: ")
# print(user)

while True:
    print(f"{player_name}\n\n {player.current_room}\n")
    user_choice = input(
        f"{player_name} where would you like to go next? North(n),South(s),East(e), West(w) or (q) to Quit: ").lower()
    if user_choice in ["n", "s", "e", "w"]:
        print("You move " + user_choice)
        if user_choice == "n":
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
            else:
                print("You hit a wall and notice you can't go that way!")
        if user_choice == "s":
            if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to
            else:
                print("You hit a wall and notice you can't go that way!")
        if user_choice == "e":
            if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to
            else:
                print("You hit a wall and notice you can't go that way!")
        if user_choice == "w":
            if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to
            else:
                print("You hit a wall and notice you can't go that way!")
    elif user_choice == "q":
        print("Goodbye and thanks for playing!")
        quit()
    else:
        print("That isn't a reconized command")
