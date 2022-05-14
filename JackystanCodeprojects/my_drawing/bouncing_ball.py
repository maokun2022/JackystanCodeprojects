"""
File: bouncing_ball.py
Name: Jacky Chang
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 0


def main():
    ball.filled = True
    window.add(ball)
    onmouseclicked(drop_ball)


def drop_ball(mouse):
    global count
    vy = 0
    if count < 3:
        if ball.x == START_X and ball.y == START_Y:
            while True:
                ball.move(VX, vy)
                vy += GRAVITY
                if ball.y <= 0 or (ball.y + SIZE) >= window.height:
                    vy = -(vy*REDUCE)
                if ball.x >= window.width:
                    window.remove(ball)
                    window.add(ball, x=START_X, y=START_Y)
                    count += 1
                    break
                pause(DELAY)


if __name__ == "__main__":
    main()
