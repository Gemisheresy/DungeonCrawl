import os

b = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
done = False
point = [0,0]
b[0][0] = 1
def grid():
    cls()
    for i in range(len(b)):
        print b[i]
def cls():
    os.system(['clear','cls'][os.name == 'nt'])
def get_current():
    return point
def move_down():
    if point[0] < 8:
        b[point[0]][point[1]] = 0
        b[point[0]+1][point[1]] = 1
        point[0] = point[0]+1
        grid()
    else:
        print "There is no more map that way"
        grid()
def move_up():
    if point[0] > 0:
        b[point[0]][point[1]] = 0
        b[point[0]-1][point[1]] = 1
        point[0] = point[0]-1
        grid()
    else:
        print "There is no more map that way"
        grid()
    
def move_left():
    if point[1] > 0 :
        b[point[0]][point[1]] = 0
        b[point[0]][point[1]-1] = 1
        point[1] = point[1]+-1
        grid()
    else:
        print "There is no more map that way"
        grid()

def move_right():
    if point[1] < 8:
        b[point[0]][point[1]] = 0
        b[point[0]][point[1]+1] = 1
        point[1] = point[1]+1
        grid()
    else:
        print "There is no more map that way"
        grid()
def start():
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
