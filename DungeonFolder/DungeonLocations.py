from DungeonItemClasses import *

class Location:
    def __init__(self,name,areaType):
        self.name = name
        self.area = area
        self.connections = {}

class LocationTile(Location):
    def __init__(self,name,areaType):
        Location.__init__(self,name,areaType)
        self.norhConnection = None
        self.eastConnection = None
        self.southConnection = None
        self.westConnection = None

class Town(Location):
    def __init__(self,name,locations=0):
        Location.__init__(self,name,'Town')
        self.locations = locations
        self.shop = Shop(town.name +' shop')

class Towntile(LocationTile):
    def __init__(self,name,description):
        LocationTile.__init__(self,name,'TownTile')

class Shop(LocationTile):
    def __init__(self,name):
        TileLocation.__init__(self,name,'Store')
        self.store = {}

        def addItem(self,Item):
            store[Item.name] = Item(Item)

class FieldTile(LocationTile):
    def __init__(self,name,description):
        LocationTile.__init__(self,name,'FieldTile')
        self.monsters= {}
        self.description = description

class Field(Location):
    def __init__(self,name,connections,tiles=0,description):
        Location.__init__(self,name,'Field')
        self.tiles = tiles
        self.location = {}
        for tile,i in range(tiles):
            location[i] = FieldLocation(field.name + i,description)
