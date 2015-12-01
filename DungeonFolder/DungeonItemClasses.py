from DungeonObject import DungeonObject

class Item(DungeonObject):
    def __init__(self,name,description,price):
        DungeonObject.__init__(self,name,'Item')
        self.description = description
        self.price = price

class Potion(Item):
    def __init__(self,name,description,price,bonus):
        Item.__init__(self,name,description,price)
        self.bonus = bonus

class Weapon(Item):
    def __init__(self,name,bonus,description,price):
        Item.__init__(self,name,'Weapon',description,price)
        self.bonus = bonus

class Chest(DungeonObject):
    def __init__(self,name,kind,items):
        DungeonObject.__init__(self,'Chest','Chest Sprite')
        self.items = items
        self.opened = False

    def openChest(self):
        self.opened = True
