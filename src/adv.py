from room import Room
from player import Player
from item import Item

# Declare all the rooms

item = {
    'gold': Item("Gold statue", """the light dances off the statue almost blindly so. The statue resembles a Roman Standard; a solid gold eagle!"""),

    'rock': Item("Rock", """On the ground is a small rock, that may be a helpful distraction or weapon"""),
}

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

room['treasure'].item_to = item['gold']
room['outside'].item_to = item['rock']


def move_to(direct, location):
    move = ''.join([direct + '_to'])
    if hasattr(location, move):
        return getattr(location, move)
    print('\n You cannot go that way')
    return location


# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player(room['outside'])

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

playing = True

while playing:
    print(f'\n Inventory: {player.inventory}')
    print(f'\n You are: {player.location.name} \n')

    if hasattr(player.location, 'item_to') and player.location.item_to.name not in player.inventory:
        print(f' You see a: {player.location.item_to.name}')
        print(f'{player.location.item_to.description} \n')

    print(player.location.description)

    if hasattr(player.location, 'item_to'):
        print('\nGo [n]orth, [e]ast, [s]outh, [w]est, [g]et')
    else:
        print('\nGo [n]orth, [e]ast, [s]outh, [w]est')

    where_to = input('Where to? ').lower()

    if where_to == 'q':
        playing = False
    elif where_to in ['n', 'e', 's', 'w', 'get']:
        player.location = move_to(where_to, player.location)
    elif where_to == "g":
        if hasattr(player.location, 'item_to')and player.location.item_to.name not in player.inventory:
            player.inventory.append(player.location.item_to.name)
    else:
        print(f'Unknown input {where_to}')
