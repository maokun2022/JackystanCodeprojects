"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.check_collision()
        # count = number of bricks == brick_rows * brick_cols, when ball touch brick once, count -= 1
        if graphics.count == 0:
            graphics.win()
            break
        # check if ball touch the left, right wall of window
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx()
        # check if ball touch the upper wall of window
        if graphics.ball.y <= 0:
            graphics.set_dy()
        # check if ball fall to bottom of window
        elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.back_to_start()
            lives -= 1
            if lives == 0:
                graphics.lose()
                break


if __name__ == '__main__':
    main()
