"""
File: my.drawing.py
Name: Jacky Chang
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GArc, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Straw Hat Crew
    As a fan of "one piece", it's my honor to draw Straw Hat Crew pirate flag by python
    Hope we would find our one piece after SC101 course!
    Copyright: Oda Eiichiro and Shueisha Inc.
    """
    window = GWindow(800, 600, title='Straw Hat Crew')
    flag = GRect(600, 400, x=(800-600)/2, y=(600-450)/2)
    flag.filled = True

    l_skull = GPolygon()
    l_skull.add_vertex((200, 130))
    l_skull.add_vertex((190, 140))
    l_skull.add_vertex((600, 340))
    l_skull.add_vertex((610, 330))
    l_skull.filled = True
    l_skull.fill_color = 'white'
    l_skull.color = 'white'

    r_skull = GPolygon()
    r_skull.add_vertex((200, 340))
    r_skull.add_vertex((190, 330))
    r_skull.add_vertex((600, 130))
    r_skull.add_vertex((610, 140))
    r_skull.filled = True
    r_skull.fill_color = 'white'
    r_skull.color = 'white'

    small_ske_1 = GOval(20, 20, x=185, y=120)
    small_ske_1.filled = True
    small_ske_1.fill_color = 'white'
    small_ske_1.color = 'white'
    small_ske_2 = GOval(20, 20, x=180, y=130)
    small_ske_2.filled = True
    small_ske_2.fill_color = 'white'
    small_ske_2.color = 'white'
    small_ske_3 = GOval(20, 20, x=595, y=120)
    small_ske_3.filled = True
    small_ske_3.fill_color = 'white'
    small_ske_3.color = 'white'
    small_ske_4 = GOval(20, 20, x=600, y=130)
    small_ske_4.filled = True
    small_ske_4.fill_color = 'white'
    small_ske_4.color = 'white'
    small_ske_5 = GOval(20, 20, x=595, y=330)
    small_ske_5.filled = True
    small_ske_5.fill_color = 'white'
    small_ske_5.color = 'white'
    small_ske_6 = GOval(20, 20, x=600, y=320)
    small_ske_6.filled = True
    small_ske_6.fill_color = 'white'
    small_ske_6.color = 'white'
    small_ske_7 = GOval(20, 20, x=185, y=330)
    small_ske_7.filled = True
    small_ske_7.fill_color = 'white'
    small_ske_7.color = 'white'
    small_ske_8 = GOval(20, 20, x=180, y=320)
    small_ske_8.filled = True
    small_ske_8.fill_color = 'white'
    small_ske_8.color = 'white'

    head = GOval(150, 150, x=(800-150)/2, y=150)
    head.filled = True
    head.fill_color = 'white'

    hat_down = GArc(150, 235, 0, 180)
    hat_down.filled = True
    hat_down.fill_color = 'yellow'

    headband = GArc(145, 200, 0, 180)
    headband .filled = True
    headband .fill_color = 'red'

    hat_up = GArc(140, 160, 0, 180)
    hat_up.filled = True
    hat_up.fill_color = 'yellow'

    l_hat_side = GArc(50, 20, 80, 190)
    l_hat_side.filled = True
    l_hat_side.fill_color = 'yellow'

    r_hat_side = GArc(50, 20, 270, 190)
    r_hat_side.filled = True
    r_hat_side.fill_color = 'yellow'

    l_eye = GOval(50, 50, x=340, y=215)
    l_eye.filled = True

    r_eye = GOval(50, 50, x=410, y=215)
    r_eye.filled = True

    nose = GOval(25, 25, x=(800-25)/2, y=265)
    nose.filled = True

    tongue = GPolygon()
    tongue.add_vertex((365, 280))
    tongue.add_vertex((340, 355))
    tongue.add_vertex((460, 355))
    tongue.add_vertex((435, 280))
    tongue.filled = True
    tongue.fill_color = 'white'

    tongue_tip = GArc(120, 200, 175, 190)
    tongue_tip.filled = True
    tongue_tip.fill_color = 'white'

    teeth = GArc(200, 150, 225, 90)
    line_1 = GLine(400, 300, 400, 355)
    line_2 = GLine(375, 295, 365, 353)
    line_3 = GLine(425, 295, 435, 353)
    label = GLabel('Straw Hat Crew')
    label.font = '-40'

    window.add(flag)
    window.add(l_skull)
    window.add(r_skull)
    window.add(small_ske_1)
    window.add(small_ske_2)
    window.add(small_ske_3)
    window.add(small_ske_4)
    window.add(small_ske_5)
    window.add(small_ske_6)
    window.add(small_ske_7)
    window.add(small_ske_8)
    window.add(tongue)
    window.add(head)
    window.add(tongue_tip, x=340, y=300)
    window.add(teeth, x=330, y=300)
    window.add(hat_down, x=(800-150)/2, y=150)
    window.add(headband, x=(800-150)/2+3, y=150)
    window.add(hat_up, x=(800-150)/2+5, y=150)
    window.add(l_hat_side, x=311, y=200)
    window.add(r_hat_side, x=310+150, y=200)
    window.add(l_eye)
    window.add(r_eye)
    window.add(nose)
    window.add(line_1)
    window.add(line_2)
    window.add(line_3)
    window.add(label, x=(800-label.width)/2, y=75)


if __name__ == '__main__':
    main()
