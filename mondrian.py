# stdlib
import tkinter
import random
from math import sqrt
from PIL import Image
import io

# third-party

# local
from rectangle import Rectangle
from similarities import calculate_structural_sim


def create_sub_rectangle(initial_rectangle, rectangles):
    """
    Recursively creates a series of sub rectangles within the initial rectangle
    passed in. The base case of the recursion is if the rectangle falls below
    an area threshold in order to prevent rectangles that are too small.
    Opposite (remaining whitespace) rectangles are calculated to ensure
    a minimum amount of 'white space' within the canvas.

    Each rectangle's color and edge thickness is chosen from a weighted
    distribution of colors and thickness. Color 'white' is the most probable
    at 50%.

    param: initial_rectangle: the rectangle to recruse on, Rectangle(Object)
    param: rectangles: the running list of rectangles, list
    """
    if initial_rectangle.calculate_area() < 100:
        return rectangles

    previous_x1 = initial_rectangle.x1
    previous_y1 = initial_rectangle.y1

    previous_x3 = initial_rectangle.x3
    previous_y3 = initial_rectangle.y3

    new_x3 = random.choice([previous_x3, random.randint(previous_x1, previous_x3)])
    if new_x3 == previous_x3:
        new_y3 = random.randint(previous_y1, previous_y3)
        opposite = Rectangle((previous_x1, new_y3), (new_x3, previous_y3), is_opposite=True)
        rectangles.append(opposite)
    else:
        new_y3 = previous_y3
        opposite = Rectangle((new_x3, previous_y1), (previous_x3, new_y3), is_opposite=True)
        rectangles.append(opposite)

    rec = canvas.create_rectangle(
        previous_x1,
        previous_y1,
        new_x3,
        new_y3,
        fill=random.choices(Rectangle.colors, [.5, .1, .1, .05, .1]),
        width=random.choices([1, 2, 4], [.8, .18, .02])
    )
    rectangle = Rectangle((previous_x1, previous_y1), (new_x3, new_y3))
    rectangles.append(rectangle)

    return create_sub_rectangle(rectangle, rectangles)

def draw():
    """
    Initially clears the canvas of all drawings/objects and generates new
    rectangles to be drawn. An initial rectangle is drawn that encompasses the
    entire canvas, then each sub rectangle is drawn recursively from the initial
    one. Finally, the function checks the list of rectangles for any ones with
    large areas -- this ensures there isn't too much 'white space' on the canvas.
    """
    canvas.delete('all')
    rectangles = []
    Rectangle.counter = 0

    initial_rectangle = Rectangle((2, 2), (1199, 599))
    rectangles.append(initial_rectangle)
    rec = canvas.create_rectangle(2, 2, 1199, 599)
    create_sub_rectangle(initial_rectangle, rectangles)
    print (rectangles)
    for rectangle in rectangles:
        if rectangle.calculate_area() > 25000 and rectangle.is_opposite:
            rectangles.remove(rectangle)
            create_sub_rectangle(rectangle, rectangles)


def save():
    """
    Saves the canvas as a jpg in /img and calculate the structural similarity
    average of the base mondrian images. Structural Sim is displayed at the
    top of the window.
    """
    ps = canvas.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save('img/test.jpg')

    average_color, average_gray = calculate_structural_sim()

    # Update label on the window to reflect averages
    label['text'] = 'ssim_color:  ' + str(average_color) + '\n' + \
                    'ssim_gray:  ' + str(average_gray)

if __name__ == '__main__':
    rectangles = []
    main_window = tkinter.Tk()
    main_window.geometry('1280x680')
    label = tkinter.Label(main_window, text="ssim_color:  \n ssim_gray:  ")
    label.pack()
    main_window.update()
    canvas = tkinter.Canvas(main_window, width=1200, height=600)
    canvas.configure(background='white')
    draw_button = tkinter.Button(main_window, text="Draw!", command=draw)
    save_button = tkinter.Button(main_window, text="Save", command=save)
    draw_button.pack()
    save_button.pack()
    canvas.pack()
    main_window.mainloop()
