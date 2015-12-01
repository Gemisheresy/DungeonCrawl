from math import floor
from random import random
from DungeonObject import DungeonObject
from DungeonLocations import *
from DungeonCharacterClass import *
from DungeonItemClasses import *
from DungeonSave import *


def makeItem(name,description,price):
    return Item(name,description,price)

def makeHero(name,strg=8,con=8,dex=8,intel=8,wis=8,cha=8):
    return HeroCharacter(name,strg,con,dex,intel,wis,cha)

def makeMonster(name,strg=8,con=8,dex=8,intel=8,wis=8,cha=8):
    return MonsterCharacter(name,strg,con,dex,intel,wis,cha)
