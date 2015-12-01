import curses
from curses import wrapper
stdscr = curses.initscr()
def main(stdscr):
    stdscr.clear()
    stdscr.addstr('Curses')
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
