import os
col = []
row = []
done = False
hero = {'point':[0,0]}
def size_grid(x,y):
    #Makes grid at size
    for i in range(x):
        col.append('0 ')
    for j in range(y):
        row.append(col[:])

def draw_grid():
    # Draws grid and clears command line
    cls()
    for i in range(len(row)):
        print(''.join(row[i]))
def cls():
    # Clears command line
    os.system(['clear','cls'][os.name == 'nt'])
def get_current():
    # Returns command line
    return hero

def move(key):
    if key == 's':
         # Moves one down
        if hero['point'][0] < len(row)- 1:
            row[hero['point'][0]][hero['point'][1]] = '0 '
            row[hero['point'][0]+1][hero['point'][1]] = '1 '
            hero['point'][0] = hero['point'][0]+1
        else:
            print("There is no more map that way")
    elif key == 'w':
         # Moves one space up
        if hero['point'][0] > 0:
            row[hero['point'][0]][hero['point'][1]] = '0 '
            row[hero['point'][0]-1][hero['point'][1]] = '1 '
            hero['point'][0] = hero['point'][0]-1
        else:
            print("There is no more map that way")
    elif key == 'a':
         # Moves one space left
        if hero['point'][1] > 0 :
            row[hero['point'][0]][hero['point'][1]] = '0 '
            row[hero['point'][0]][hero['point'][1]-1] = '1 '
            hero['point'][1] = hero['point'][1]+-1
        else:
            print("There is no more map that way")
    elif key == 'd':
          # Moves one space right
        if hero['point'][1] < len(col)- 1:
            row[hero['point'][0]][hero['point'][1]] = '0 '
            row[hero['point'][0]][hero['point'][1]+1] = '1 '
            hero['point'][1] = hero['point'][1]+1
        else:
            print("There is no more map that way")
    elif key == 'e':
            done = True

    
def start():
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
    size_grid(wide,height)
    row[0][0] = '1 '
    draw_grid()
    while done == False:
        way = str(input('Where do you want to go? '))
        if way == 'e':
            done = True
            cls()
        else:
            move(way)
        draw_grid()
start()
