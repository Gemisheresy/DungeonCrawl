import os

b = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
done = False
point = [0,0]
b[0][0] = 1
def cls():
    # Clears the command line
    os.system(['clear','cls'][os.name == 'nt'])
def grid():
    # Clears the command line before drawing the grid
    cls()
    for i in range(len(b)):
        print b[i]
def get_current():
    # Returns the current location of the point.This will be for a feature later
    return point
def move_down():
    # Moves the point -1 on the y axis. Redraws gird
    if point[0] < 8:
        b[point[0]][point[1]] = 0
        b[point[0]+1][point[1]] = 1
        point[0] = point[0]+1
    else:
        print "There is no more map that way"
    grid()
def move_up():
    # Moves the point 1 on the y axis. Redraws grid
    if point[0] > 0:
        b[point[0]][point[1]] = 0
        b[point[0]-1][point[1]] = 1
        point[0] = point[0]-1
    else:
        print "There is no more map that way"
    grid()
    
def move_left():
     # Moves the point -1 on the x axis. Redraws grid
    if point[1] > 0 :
        b[point[0]][point[1]] = 0
        b[point[0]][point[1]-1] = 1
        point[1] = point[1]+-1
    else:
        print "There is no more map that way"
    grid()

def move_right():
     # Moves the point 1 on the x axis. Redraws grid
    if point[1] < 8:
        b[point[0]][point[1]] = 0
        b[point[0]][point[1]+1] = 1
        point[1] = point[1]+1
    else:
        print "There is no more map that way"
    grid()
def start():
    #Draws first grid and starts loop for game.
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
