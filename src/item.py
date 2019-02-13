

class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def __str__(self):
        return(f'This is a {self.item_name} which {self.item_description} ')
