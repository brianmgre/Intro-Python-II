from room import Room
from player import Player
from item import Item

# Declare all the rooms

# item = {
#     'gold': Item("Gold statue", """the light dances off the statue almost blindly so. The statue resembles a Roman Standard; a solid gold eagle!"""),

#     'rock': Item("Rock", """On the ground is a small rock. It may be a helpful distraction or weapon"""),
# } 

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Rock", """a small rock. It may be a helpful distraction or weapon""")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Rock", """a small rock. It may be a helpful distraction or weapon""")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Gold statue", """the light dances off the statue almost blindly so. The statue resembles a Roman Standard; a solid gold eagle!""")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Rock", """a small rock. It may be a helpful distraction or weapon""")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Rock", """a small rock. It may be a helpful distraction or weapon""")]),
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

# room['overlook'].items = item['gold']
# room['outside'].items = item['rock']


def move_to(direct, location):
    move = ''.join([direct + '_to'])
    if hasattr(location, move):
        return getattr(location, move)
    print('\n You cannot go that way')
    return location

def add_item(player, item):
    player.get_item(item)
    player.location.delete(item)

def look(player, location):
    player.location.look_around()

def closer_look(player, location):
    player.location.inspect()

def drop_item(player, item):
    player.remove_item(item)

# Main
#

name = input('What is your name? ')
player = Player(name, room['outside'])

playing = True

while playing:
    print(f'\n Inventory: {player.inventory}')
    print(f'\n {player.name}, you are: {player.location.name} \n')
    print(player.location.description)
    print('\nGo [n]orth, [e]ast, [s]outh, [w]est, [l]ook around, [d]rop item')
    
    where_to = input('Where to? ').lower()
    if where_to == 'q':
        playing = False

    elif where_to in ['n', 'e', 's', 'w']:
        player.location = move_to(where_to, player.location)

    elif where_to == 'l':
        if len(player.location.items) > 0:
            look(player, player.location)
            inspect = input(f'\n[i]nspect {player.location.items[0].name} or [l]eave it? ')
                
            if inspect == 'i':
                closer_look(player, player.location.items[0].name)
                take = input(f'\n [t]take the {player.location.items[0].name} or [l]eave it? ').lower()

                if take == 't' and player.location.items[0].name not in player.inventory:
                    add_item(player, player.location.items[0].name)
                else:
                    print(f'you already have the {player.location.items[0].name}')
        else:
            print('\n There is nothing here')
    
    elif where_to == 'd':
        if len(player.inventory) == 0:
            print("\nyou don't have anything to drop")
        else:
            drop = input(f'\n What item out of inventory would you like to drop? ').lower().capitalize()
            drop_item(player, drop)

    else:
        print(f'Unknown input {where_to}')
