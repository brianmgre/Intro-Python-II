# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        

    def __str__(self):
        return(f'{self.name}, {self.description}')

    def look_around(self):
        if self.items[0].name == None:
            print ('there is nothing here')
        else:
            print(f"You see a {self.items[0].name}")

    def inspect(self):
        if self.items[0].name == None:
            print("Why do you want me to inspect nothing")
        else:
            print(f'\ntaking a closer look you see {self.items[0].description}')

    def delete(self, item):
        self.items[0].name = None
        self.items[0].description = None

        