"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.2

# Controls the upper bound for black pixel
BLACK = 120


def main():
    """
    我在001課程後對程式語言產生爆炸般想法，寫作業時屢屢"獻上心臟"
    """
    fig = SimpleImage('image_contest/JACKY_2.JPG') # 1806*3212
    fig.show()
    bg = SimpleImage('image_contest/JACKY_bg.jpg') # 299*169
    bg.make_as_big_as(fig) # 1806*3212
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue)//3
            total = fig_pixel.red + fig_pixel.green + fig_pixel.blue
            if fig_pixel.green > avg * THRESHOLD and total > BLACK:
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig


if __name__ == '__main__':
    main()
