import os
a = []
b = []
done = False
point = [0,0]
def size_grid(x,y):
    #Makes grid at size
    for i in range(x):
        a.append(0)
    for j in range(y):
        b.append(a[:])

def grid():
    # Draws grid and clears command line
    cls()
    for i in range(len(b)):
        print b[i]
def cls():
    # Clears command line
    os.system(['clear','cls'][os.name == 'nt'])
def get_current():
    # Returns command line
    return point
def move_down():
    # Moves one down
    if point[0] < len(b )- 1:
        b[point[0]][point[1]] = 0
        b[point[0]+1][point[1]] = 1
        point[0] = point[0]+1
        grid()
    else:
        print "There is no more map that way"
        grid()
def move_up():
    # Moves one space up
    if point[0] > 0:
        b[point[0]][point[1]] = 0
        b[point[0]-1][point[1]] = 1
        point[0] = point[0]-1
        grid()
    else:
        print "There is no more map that way"
        grid()
    
def move_left():
    # Moves one space left
    if point[1] > 0 :
        b[point[0]][point[1]] = 0
        b[point[0]][point[1]-1] = 1
        point[1] = point[1]+-1
        grid()
    else:
        print "There is no more map that way"
        grid()

def move_right():
    # Moves one space right
    if point[1] < len(a)- 1:
        b[point[0]][point[1]] = 0
        b[point[0]][point[1]+1] = 1
        point[1] = point[1]+1
        grid()
    else:
        print "There is no more map that way"
        grid()
def start():
    wide = int(raw_input("How wide do you want the room? "))
    height= int(raw_input("How High do you want the room? "))
    size_grid(wide,height)
    b[0][0] = 1
    grid()
    done = False
    while done == False:
        answer=raw_input("where would you like to go?\n")
        if answer == 'a':
            move_left()
        elif answer == 'd':
            move_right()
        elif answer == 'w':
            move_up()
        elif answer == 's':
            move_down()
        elif answer == 'e':
            done = True

start()
