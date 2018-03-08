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


def create_sub_rectangle(initial_rectangle, rectangles, area_limit=1000):
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
    if initial_rectangle.calculate_area() < area_limit:
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

    return create_sub_rectangle(rectangle, rectangles, area_limit=area_limit)


def draw(area_limit=2000, opposite_area_limit=2000):
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
    create_sub_rectangle(initial_rectangle, rectangles, area_limit=area_limit)

    for rectangle in rectangles:
        if rectangle.calculate_area() > opposite_area_limit and rectangle.is_opposite:
            rectangles.remove(rectangle)
            create_sub_rectangle(rectangle, rectangles, area_limit=area_limit)


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

    return average_color, average_gray


def highest_ssim():
    """
    Simulation that runs through multiple levels of threshholds for area
    limits. After each one is drawn and saved, the average is recorded.
    At the end of the simulation the highest average for both color and
    grayscale are displayed as well as their corresponding threshholds.
    """
    highest_avg_color = (0, (0, 0))
    highest_avg_gray = (0, (0, 0))

    for x in range(1000, 200000, 10000):
        for y in range(1000, 200000, 10000):
            print(f"Highest color: {highest_avg_color}, Highest gray: {highest_avg_gray}")
            iterations = 0
            while iterations < 3:
                draw(x, y)
                average_color, average_gray = save()

                if highest_avg_color[0] < average_color:
                    highest_avg_color = (average_color, (x, y))
                if highest_avg_gray[0] < average_gray:
                    highest_avg_gray = (average_gray, (x, y))

                iterations += 1

    print(f"Simulation completed with \
            Highest color: {highest_avg_color}, Highest gray: {highest_avg_gray}")


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
    simulation_button = tkinter.Button(main_window, text="Run Sim", command=highest_ssim)
    simulation_button.pack()
    draw_button.pack()
    save_button.pack()
    canvas.pack()
    main_window.mainloop()
