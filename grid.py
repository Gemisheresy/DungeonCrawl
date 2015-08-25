import os
import random
import math
col = []
row = []
done = False
hero = {'point':[0,0],
        'attack': 1,
        'health':10,
        'speed': 1}
monster = {'point':[0,0],
           'attack' : 1,
           'health' : 10,
           'speed' : 1}
direction = {'a':'Right',
             'd':'Left',
             'w':'Up',
             's':'Down',
             'facing':''}
phrase = {'moved':'You explore this area and find nothing.',
          'bounds':'There is no where to go that way.',
          'damaged':'You hit the monster in front of you.',
          'missed':'You swung and missed.',
          'defeated':' You defeated the monster, press e to exit the dungeon.',
          'monster': 'There is a big snarling monster in front of you.',
          'last':''} 

def size_grid(x,y):
    #Makes grid at size
    for i in range(x):
        col.append('0 ')
    for j in range(y):
        row.append(col[:])
def random_spot(num):
    return int(math.floor(random.random() * num)+1)

def draw_grid():
    cls()
    for i in range(len(row)):
        print(''.join(row[i]))

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def get_current():
    return hero

def change_last(key):
    direction['facing'] = direction.get(key)
   
def get_last():
    return direction['facing']

def change_phrase(action):
    phrase['last'] = phrase.get(action)


def move(key):
# moves the hero one space down
    change_last(key)
    if key == 's':
        if hero['point'][0] < len(row)- 1:
            if row[hero['point'][0]+1][hero['point'][1]] =='X ':
                change_phrase('monster')
            elif row[hero['point'][0]+1][hero['point'][1]] == '0 ':
                row[hero['point'][0]][hero['point'][1]] = '0 '
                row[hero['point'][0]+1][hero['point'][1]] = '1 '
                hero['point'][0] = hero['point'][0]+1
                change_phrase('moved')
        else:
                change_phrase('bounds')
# moves the hero one space up
    elif key == 'w':
        if hero['point'][0] > 0:
            if row[hero['point'][0]-1][hero['point'][1]] =='X ':
                change_phrase('monster')
            elif row[hero['point'][0]-1][hero['point'][1]] == '0 ':
                row[hero['point'][0]][hero['point'][1]] = '0 '
                row[hero['point'][0]-1][hero['point'][1]] = '1 '
                hero['point'][0] = hero['point'][0]-1
                change_phrase('moved')
        else:
                change_phrase('bounds')
# moves the hero one space left
    elif key == 'a':
        if hero['point'][1] > 0 :
            if row[hero['point'][0]][hero['point'][1]-1] =='X ':
                change_phrase('monster')
            elif row[hero['point'][0]][hero['point'][1]-1] == '0 ':
                row[hero['point'][0]][hero['point'][1]] = '0 '
                row[hero['point'][0]][hero['point'][1]-1] = '1 '
                hero['point'][1] = hero['point'][1]-1
                change_phrase('moved')
        else:
                change_phrase('bounds')
# moves the hero one space right
    elif key == 'd':
        if hero['point'][1] < len(row)- 1:
            if row[hero['point'][0]][hero['point'][1]+1] =='X ':
                change_phrase('monster')
            elif row[hero['point'][0]][hero['point'][1]+1] == '0 ':
                row[hero['point'][0]][hero['point'][1]] = '0 '
                row[hero['point'][0]][hero['point'][1]+1] = '1 '
                hero['point'][1] = hero['point'][1]+1
                change_phrase('moved')
        else:
                change_phrase('bounds')
    
    
def attack():
# checks last direction moved to if monster is in front of hero
    if direction['facing'] == 'Left':
        if row[hero['point'][0]][hero['point'][1] - 1] == 'X ':
            change_phrase('damaged')
            monster['health'] -= hero['attack']
        else:
            change_phrase('missed')
            
    elif direction['facing'] == 'Down':
        if row[hero['point'][0]+1][hero['point'][1]] == 'X ':
            change_phrase('damaged')
            monster['health'] -= hero['attack']
        else:
            change_phrase('missed')
            
    elif direction['facing'] == 'Up':
        if row[hero['point'][0]  - 1][hero['point'][1]] == 'X ':
            change_phrase('damaged')
            monster['health'] -= hero['attack']
        else:
            change_phrase('missed')
            
    elif direction['facing'] == 'Right':
        if row[hero['point'][0]][hero['point'][1]+1] == 'X ':
            change_phrase('damaged')
            monster['health'] -= hero['attack']
        else:
            change_phrase('missed')

def start():
# starts game by creating to loops
    done = False
    while True:
        try:
            wide = int(input("How wide do you want the room? "))
            break
        except ValueError:
            print('Thate wasnt a number try again')
    while True:
        try:
            height = int(input("How high do you want the room? "))
            break
        except ValueError:
            print('That wasnt a number try again')
    if wide >= 25:
        wide = 25
    if height >= 25:
        height = 25
    size_grid(wide,height)
    row[hero['point'][0]][hero['point'][1]] = '1 '
    monster['point'][0] = random_spot(wide-1)
    monster['point'][1] = random_spot(height-1)
    row[monster['point'][0]][monster['point'][1]] = 'X '
    draw_grid()
    while done == False:
        way = str(input('Where do you want to go? '))
        if way == 'e':
            done = True
            cls()
        elif way == 'x':
            attack()
        else:
            move(way)
        if monster['health'] == 0:
            row[monster['point'][0]][monster['point'][1]] = '0 '
            change_phrase('defeated')
        draw_grid()
        print(phrase['last'])
start()



        
        
        
