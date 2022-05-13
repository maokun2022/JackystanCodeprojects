"""
File: babygraphics.py
Name: Jacky Chang
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'magenta']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    real_width = width - GRAPH_MARGIN_SIZE*2
    x_coordinate = GRAPH_MARGIN_SIZE + real_width*((year_index-YEARS[0])/10)/len(YEARS)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=LINE_WIDTH)
    canvas.create_line(CANVAS_WIDTH-GRAPH_MARGIN_SIZE, 0, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT,
                       width=LINE_WIDTH)
    for year in YEARS:
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year), 0, get_x_coordinate(CANVAS_WIDTH, year),
                           CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=year, anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    count = 0
    for name in lookup_names:
        # if count % 4 == 0:
        #     color = COLORS[0]
        #     count += 1
        # elif count % 4 == 1:
        #     color = COLORS[1]
        #     count += 1
        # elif count % 4 == 2:
        #     color = COLORS[2]
        #     count += 1
        # else:
        #     color = COLORS[3]
        #     count += 1
        color = COLORS[count % len(COLORS)]
        count += 1
        for year in YEARS:
            year_txt = str(year)
            if year == YEARS[0]:
                # for plot 1st point
                # if the rank is <= 1000 --> add text based on the rank in 1st year rank in TEARS,
                # otherwise add text at bottom margin line
                if year_txt not in name_data[name]:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       text=name + '*', anchor=tkinter.SW, fill=color)
                    y_cor = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    # For next line plotting, y coordinate of this text is recorded by a variable
                else:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year)+TEXT_DX,
                                       GRAPH_MARGIN_SIZE+(int(name_data[name][year_txt])/MAX_RANK)*(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)
                                       , text=name + name_data[name][year_txt], anchor=tkinter.SW, fill=color)
                    y_cor = GRAPH_MARGIN_SIZE+(int(name_data[name][year_txt])/MAX_RANK)*(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)
                    # For next line plotting, y coordinate of this text is recorded by a variable
            else:
                # Plot next point first, then create line between this point and previous point
                # Also need to check if rank is <= each time
                if year_txt not in name_data[name]:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       text=name + '*', anchor=tkinter.SW, fill=color)
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH, year-10), y_cor, width=LINE_WIDTH, fill=color)
                    y_cor = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    # For next line plotting, y coordinate of this text is recorded by a variable
                else:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year)+TEXT_DX,
                                       GRAPH_MARGIN_SIZE+(int(name_data[name][year_txt])/MAX_RANK)*(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)
                                       , text=name + name_data[name][year_txt], anchor=tkinter.SW, fill=color)
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year),
                                       GRAPH_MARGIN_SIZE+(int(name_data[name][year_txt])/MAX_RANK)*(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE),
                                       get_x_coordinate(CANVAS_WIDTH, year-10), y_cor, width=LINE_WIDTH, fill=color)
                    y_cor = GRAPH_MARGIN_SIZE+(int(name_data[name][year_txt])/MAX_RANK)*(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)
                    # For next line plotting, y coordinate of this text is recorded by a variable


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
