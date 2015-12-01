import curses
from curses import wrapper
from grid import *
stdscr = curses.initscr()
stdscr.keypad(True)


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
    if monster['point'] == hero['point']:
        monster['point'][0] = random_spot(wide-1)
        monster['point'][1] = random_spot(height-1)
    sword['point'][0] = random_spot(wide-1)
    sword['point'][1] = random_spot(height-1)
    if sword['point'] == monster['point'] or hero['point']:
        sword['point'][0] = random_spot(wide-1)
        sword['point'][1] = random_spot(height-1)
    row[monster['point'][0]][monster['point'][1]] = 'X '
    row[sword['point'][0]][sword['point'][0]] = '+ '
    draw_grid()
    while done == False:
        stdscr.echo()
        stdscr.cbreak()
        print("where do you want to go")
        way = curses.getkey()
        if way == 'e':
            done = True
            cls()
        elif way == 'x':
            attack()
        else:
            move(way)
        if monster['health'] <= 0:
            row[monster['point'][0]][monster['point'][1]] = '0 '
            if hero['point'] == monster['point']:
                row[monster['point'][0]][monster['point'][1]] = '1 '
            change_phrase('defeated')
        draw_grid()
        print(phrase['last'])
        print(hero['attack'])
        print(monster['health'])
def main(stdscr):
    stdscr.clear()
    start()

if __name__ == '__main__':
    wrapper(main)
