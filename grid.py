import os
import random
import math
col = []
row = []
done = False
response = {'phrase' :'', 'last':''}
hero = {'point':[0,0], 'attack': 1,'health' : 10, 'speed': 1}
monster = {'point': [0,0],'attack' : 1, 'health' : 10, 'speed' : 1}

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

def change_response_last(key):
# changes the last direction variable for attacking and phrases
    if key == 'a':
        response['last'] = 'Left'
    elif key == 'd':
        response['last'] = 'Right'
    elif key == 'w':
        response['last'] = 'Up'
    elif key == 's':
        response['last'] = 'Down'

def change_response_phrase(action):
# changes the phrase displayed to the user on the screen.
    if action == 'moved':
        response['phrase'] = 'The last way you moved was ' + response['last']
    elif action == 'outofbounds':
        response['phrase'] = 'There is no where to go that way'
    elif action == 'damaged':
        response['phrase'] = 'You hit the monster in front of you'
    elif action == 'missed':
        response['phrase'] = 'You swing and miss'
    elif action == 'defeated':
        response['phrase'] = 'You defeated the monster. Press e to end the game'
    elif action == 'monster':
        response['phrase'] = 'There is a big snarling monster infront of you'

def move(key):
# moves the hero one space down
    if key == 's':
        change_response_last(key)
        if hero['point'][0] < len(row)- 1:
            if row[hero['point'][0]+1][hero['point'][1]] =='X ':
                change_response_phrase('monster')
            elif row[hero['point'][0]+1][hero['point'][1]] == '0 ':
                row[hero['point'][0]][hero['point'][1]] = '0 '
                row[hero['point'][0]+1][hero['point'][1]] = '1 '
                hero['point'][0] = hero['point'][0]+1
                change_response_phrase('moved')
        else:
                change_response_phrase('outofbounds')
# moves the hero one space up
    elif key == 'w':
        change_response_last(key)
        if hero['point'][0] > 0:
            if row[hero['point'][0]-1][hero['point'][1]] =='X ':
                change_response_phrase('monster')
            elif row[hero['point'][0]-1][hero['point'][1]] == '0 ':
                row[hero['point'][0]][hero['point'][1]] = '0 '
                row[hero['point'][0]-1][hero['point'][1]] = '1 '
                hero['point'][0] = hero['point'][0]-1
                change_response_phrase('moved')
        else:
                change_response_phrase('outofbounds')
# moves the hero one space left
    elif key == 'a':
        change_response_last(key)
        if hero['point'][1] > 0 :
            if row[hero['point'][0]][hero['point'][1]-1] =='X ':
                change_response_phrase('monster')
            elif row[hero['point'][0]][hero['point'][1]-1] == '0 ':
                row[hero['point'][0]][hero['point'][1]] = '0 '
                row[hero['point'][0]][hero['point'][1]-1] = '1 '
                hero['point'][1] = hero['point'][1]-1
                change_response_phrase('moved')
        else:
                change_response_phrase('outofbounds')
# moves the hero one space right
    elif key == 'd':
        change_response_last(key)
        if hero['point'][1] < len(row)- 1:
            if row[hero['point'][0]][hero['point'][1]+1] =='X ':
                change_response_phrase('monster')
            elif row[hero['point'][0]][hero['point'][1]+1] == '0 ':
                row[hero['point'][0]][hero['point'][1]] = '0 '
                row[hero['point'][0]][hero['point'][1]+1] = '1 '
                hero['point'][1] = hero['point'][1]+1
                change_response_phrase('moved')
        else:
                change_response_phrase('outofbounds')

def attack():
# checks last direction moved to if monster is in front of hero
    if response['last'] == 'Left':
        if row[hero['point'][0]][hero['point'][1] - 1] == 'X ':
            change_response_phrase('damaged')
            monster['health'] -= hero['attack']
        else:
            change_response_phrase('missed')
            
    elif response['last'] == 'Down':
        if row[hero['point'][0]+1][hero['point'][1]] == 'X ':
            change_response_phrase('damaged')
            monster['health'] -= hero['attack']
        else:
            change_response_phrase('missed')
            
    elif response['last'] == 'Up':
        if row[hero['point'][0]  - 1][hero['point'][1]] == 'X ':
            change_response_phrase('damaged')
            monster['health'] -= hero['attack']
        else:
            change_response_phrase('missed')
            
    elif response['last'] == 'Right':
        if row[hero['point'][0]][hero['point'][1]+1] == 'X ':
            change_response_phrase('damaged')
            monster['health'] -= hero['attack']
        else:
            change_response_phrase('missed')

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
            change_response_phrase('deafated')
        draw_grid()
        print(response['phrase'])
start()



        
        
        
