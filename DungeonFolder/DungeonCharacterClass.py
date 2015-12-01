from DungeonObject import DungeonObject

class CharacterObject(DungeonObject):
    def __init__(self,name,kind,strg,con,dex,intel,wis,cha):
        DungeonObject.__init__(self,name,kind)
        self.strg = strg
        self.con = con
        self.dex = dex
        self.intel = intel
        self.wis = wis
        self.cha = cha
        self.inventory = Inventory()

    def addItem(self,Item):
        self.inventory.addItem(self.Inventory,Item)

class HeroCharacter(CharacterObject):
    def __init__(self,name,strg,con,dex,intel,wis,cha):
        CharacterObject.__init__(self,name,'Hero',strg,con,dex,intel,wis,cha)

class MonsterCharacter(CharacterObject):
    def __init__(self,name,strg,con,dex,intel,wis,cha):
        CharacterObject.__init__(self,name,'Monster',strg,con,dex,intel,wis,cha)

class Inventory:
    def __init__(self,slots=10,opened=False):
        self.items = {}
        self.gold = 0
    def openInventory(self):
        self.opened = True

    def closeInventory(self):
        self.opened = False

    def addItem(self,Item):
        self.items[Item.name] = Item
