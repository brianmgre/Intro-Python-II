

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player, name):
        player.inventory.append(name)

    def __str__(self):
        return(f'This is a {self.name} which {self.description} ')
