"""
File: draw_line.py
Name: Jacky Chang
-------------------------
This file make a "hole circle" when user click on 1,3,5th time.
And a line will be drawn when user click on 1,3,5th time, the lines are drawn by click 1-2, 3-4, 5-6 etc
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# This control the size of circle when user click on 1,3,5th time.
SIZE = 10

# global variable
window = GWindow()
hole = GOval(SIZE, SIZE)
random_x = int
random_y = int
count = 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    """
    param mouse: mouse event, store mouse information
    """
    global count
    if count % 2 == 1:
        hole.color = 'black'
        window.add(hole, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        count += 1
    elif count % 2 == 0:
        line = GLine(hole.x, hole.y, mouse.x, mouse.y)
        window.add(line)
        window.remove(hole)
        count += 1


if __name__ == "__main__":
    main()
