# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []


    def get_item(self, item):
        if item == None:
            return
        else:
            self.inventory.append(item)

    def remove_item(self, item):
        # x = self.inventory.index(item)
        if item not in self.inventory:
            print('\nYou do not have that item in inventory')
        else:
            self.inventory.remove(item)
            print(f'\nYour {item} is dropped and smashes into a thousand pieces on the floor')

