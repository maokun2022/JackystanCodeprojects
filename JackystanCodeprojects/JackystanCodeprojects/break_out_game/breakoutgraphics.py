"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10      # Number of rows of bricks
BRICK_COLS = 10     # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=(self.window_height - paddle_offset -
                                                                              paddle_height))
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-ball_radius)/2, y=(self.window_height-ball_radius)/2)
        self.ball_radius = ball_radius

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.drop_ball)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j % 10 <= 1:
                    self.brick.fill_color = 'red'
                elif j % 10 <= 3:
                    self.brick.fill_color = 'orange'
                elif j % 10 <= 5:
                    self.brick.fill_color = 'yellow'
                elif j % 10 <= 7:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=i*(brick_width+brick_spacing),
                                y=brick_offset+j*(brick_height+brick_spacing))
        self.count = brick_cols * brick_rows

    def paddle_move(self, event):
        """
        :param event: mouseevent, mousedragging
        :return: paddle moving
        """
        if event.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif event.x >= self.window_width - self.paddle.width/2:
            self.paddle.x = self.window_width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2

    def set_dx(self):
        self.__dx = - self.__dx

    def set_dy(self):
        self.__dy = - self.__dy

    def drop_ball(self, event):
        """
        :param event: mouseevent, mouseclick
        :return: drop ball, start game
        """
        if self.__dy == 0 and self.__dx == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
            self.__dy = INITIAL_Y_SPEED

    def back_to_start(self):
        self.ball.x = (self.window_width - self.ball_radius)/2
        self.ball.y = (self.window_height - self.ball_radius)/2
        self.__dx = 0
        self.__dy = 0

    def check_collision(self):
        # count = 0
        for i in range(2):
            for j in range(2):
                may_obj = self.window.get_object_at(self.ball.x+i*self.ball_radius*2, self.ball.y+j*self.ball_radius*2)
                if may_obj is not None:
                    if may_obj is not self.paddle:  # touch brick
                        self.window.remove(may_obj)
                        self.__dy = - self.__dy
                        self.count -= 1
                        return
                    else:  # touch paddle
                        self.__dy = - INITIAL_Y_SPEED
                        # to make sure that ball will go up when any point of ball touch paddle
                        return

        # getter
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def win(self):
        if self.count == 0:
            label = GLabel('You Win!')
            label.font = '-40'
            self.window.add(label, x=(self.window_width - label.width) / 2,
                            y=(self.window_height - label.height) / 2)
            self.window.remove(self.ball)

    def lose(self):
        label = GLabel('Game Over!')
        label.font = '-40'
        self.window.add(label, x=(self.window_width-label.width)/2, y=(self.window_height-label.height)/2)
        self.window.remove(self.ball)