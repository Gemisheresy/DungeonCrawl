import os
col = []
row = []
done = False
point = [0,0]
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
    return point

def move(key):
    if key == 's':
         # Moves one down
        if point[0] < len(row)- 1:
            row[point[0]][point[1]] = '0 '
            row[point[0]+1][point[1]] = '1 '
            point[0] = point[0]+1
        else:
            print("There is no more map that way")
    elif key == 'w':
         # Moves one space up
        if point[0] > 0:
            row[point[0]][point[1]] = '0 '
            row[point[0]-1][point[1]] = '1 '
            point[0] = point[0]-1
        else:
            print("There is no more map that way")
    elif key == 'a':
         # Moves one space left
        if point[1] > 0 :
            row[point[0]][point[1]] = '0 '
            row[point[0]][point[1]-1] = '1 '
            point[1] = point[1]+-1
        else:
            print("There is no more map that way")
    elif key == 'd':
          # Moves one space right
        if point[1] < len(col)- 1:
            row[point[0]][point[1]] = '0 '
            row[point[0]][point[1]+1] = '1 '
            point[1] = point[1]+1
        else:
            print("There is no more map that way")
    elif key == 'e':
            done = True

    
def start():
    while True:
        try:
            wide = int(raw_input("How wide do you want the room? "))
            break
        except ValueError:
            print('Thate wasnt a number try again')
    while True:
        try:
            height = int(raw_input("How high do you want the room? "))
            break
        except ValueError:
            print('That wasnt a number try again')
    size_grid(wide,height)
    row[0][0] = '1 '
    draw_grid()
    while done == False:
        move(str(raw_input('Where do you want to go? ')))
        draw_grid()
start()
