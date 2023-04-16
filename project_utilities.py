import os
import random
import math


list_of_colors = ['alice blue', 'antique white', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanched almond', 'blue', 'blue violet', 'brown', 'burlywood', 'cadet blue', 'chartreuse', 'chocolate', 'coral', 'cornflower blue', 'cornsilk', 'crimson', 'cyan', 'dark blue', 'dark cyan', 'dark goldenrod', 'dark gray', 'dark grey', 'dark green', 'dark khaki', 'dark magenta', 'dark olive green', 'dark orange', 'dark orchid', 'dark red', 'dark salmon', 'dark sea green', 'dark slate blue', 'dark slate gray', 'dark slate grey', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dim grey', 'dodger blue', 'firebrick', 'floral white', 'forest green', 'gainsboro', 'ghost white', 'gold', 'goldenrod', 'gray', 'grey', 'green', 'green yellow', 'honeydew', 'hot pink', 'indian red', 'ivory', 'khaki', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light goldenrod yellow', 'light gray', 'light grey', 'light green', 'light pink', 'light salmon', 'light sea green', 'light sky blue', 'light slate gray', 'light slate grey', 'light steel blue', 'light yellow', 'lime green', 'linen', 'magenta', 'maroon', 'medium aquamarine', 'medium blue', 'medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'moccasin', 'navajo white', 'navy', 'old lace', 'olive', 'olive drab', 'orange', 'orange red', 'orchid', 'pale goldenrod', 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'peru', 'pink', 'plum', 'powder blue', 'purple', 'red', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'sandy brown', 'sea green', 'seashell', 'sienna', 'silver', 'sky blue', 'slate blue', 'slate gray', 'slate grey', 'snow', 'spring green', 'steel blue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'white smoke', 'yellow', 'yellow green']


__all__ = [
    "make_circle", "make_oval", "make_square", "make_rectangle", "make_line",
    "make_car", "make_cloud", "make_grid", "make_image", "get_top", "get_left",
    "get_right", "get_left", "get_center", "get_bottom", "get_tag_from_event",
    "update_position", "update_fill", "delete", "flip", "rotate"
]

_cache = []
def _get_coordinates(canvas, id):
    return canvas.coords(id)

def _set_coordinates(canvas, id, coordinates):
    canvas.coords(id, coordinates)

def _update_position_by_id(canvas, id, x=2, y=0):
    coords = _get_coordinates(canvas, id)
    # update coordinates:
    for i in range(0, len(coords)):
        if i % 2 == 0:
            coords[i] += x
        else:
            coords[i] += y
    # set the coordinates:
    _set_coordinates(canvas, id, coords)

def _get_x_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='x')

def _get_y_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='y')

def _get_coordinates_by_dimension(canvas, tag, dimension='x'):
    '''
    updates the x and y position of all shapes that have been tagged
    with the tag argument
    '''
    if dimension == 'x':
        pos = 0
    else:
        pos = 1
    shape_ids = canvas.find_withtag(tag)
    coords = []
    for id in shape_ids:
        shape_coords = _get_coordinates(canvas, id)
        for i in range(0, len(shape_coords)):
            if i % 2 == pos:
                coords.append(shape_coords[i])
    return coords

def make_circle(canvas, center, radius, fill_color='white', tag=None, stroke_width=2, outline=None):
    '''
    Draws a circle on a specified canvas with a particular center and radius. It does not use the `create_oval`
    function so that it can be rotated by the `rotate` function.

    * `canvas` (`Canvas`): [Required] The `Canvas` to draw on.
    * `center` (`tuple`): [Required] A `(x,y)` coorindate marking the center of the shape.
    * `radius` (`float` or `int`): [Required] The radius of the shape.
    * `fill_color` (`str`): Color name or hex code to fill the object with.
    * `tag` (`str`): The tag with which to name the object being drawn.
    * `stroke_width` (`int`): How wide to draw the outline of the shape.
    * `outline` (`str`): Color name or hex code used to outline the shape.

    Returns an objectID `(int)`.
    '''
    return make_poly_oval(
        canvas, center, radius, radius, fill_color=fill_color, tag=tag,
        stroke_width=stroke_width, outline=outline
    )

def make_oval(canvas, center, radius_x, radius_y, fill_color='#FF4136', tag=None, stroke_width=1, outline=None):
    '''
    Draws a circle on a specified canvas with a particular center and radius. It does not use the `create_oval`
    function so that it can be rotated by the `rotate` function.

    * `canvas` (`Canvas`): [Required] The `Canvas` to draw on.
    * `center` (`tuple`): [Required] A `(x,y)` coorindate marking the center of the shape.
    * `radius_x` (`float` or `int`): [Required] The radius of the shape in the x-axis.
    * `radius_y` (`float` or `int`): [Required] The radius of the shape in the y-axis.
    * `fill_color` (`str`): Color name or hex code to fill the object with.
    * `tag` (`str`): The tag with which to name the object being drawn.
    * `stroke_width` (`int`): How wide to draw the outline of the shape.
    * `outline` (`str`): Color name or hex code used to outline the shape.

    Returns an objectID `(int)`.
    '''
    return make_poly_oval(
        canvas,
        center,
        radius_x,
        radius_y,
        fill_color=fill_color,
        tag=tag,
        stroke_width=stroke_width,
        outline=outline)
    

def make_poly_circle(canvas, center, radius, fill_color='white', tag=None, stroke_width=1, outline=None):
    return make_poly_oval(
        canvas,
        center,
        radius,
        radius,
        fill_color=fill_color,
        tag=tag,
        stroke_width=stroke_width,
        outline=outline)

def make_poly_oval(canvas, center, radius_x, radius_y, fill_color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    x0, y0, x1, y1 = (x - radius_x, y - radius_y, x + radius_x, y + radius_y)

    steps = 100
    # major and minor axes
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0

    # center
    xc = x0 + a
    yc = y0 + b

    point_list = []

    # create the oval as a list of points
    for i in range(steps):
        # Calculate the angle for this step
        theta = (math.pi * 2) * (float(i) / steps)

        x = a * math.cos(theta)
        y = b * math.sin(theta)

        point_list.append(round(x + xc))
        point_list.append(round(y + yc))

    return canvas.create_polygon(
        point_list,
        fill=fill_color,
        width=stroke_width,
        tags=tag,
        outline=outline,
        smooth=True
    )

def rotate(canvas, tag, degrees=5, origin=None):
    '''
    Rotates any polygons with a given tag around a point on a given canvas. Note that this does
    not work with circles or ovals generated using the `create_oval`/`create_circle` functions.

    * `canvas` (`Canvas`): [Required] The `Canvas` to draw on.
    * `tag` (`str`): The tag of the object to animate.
    * `degrees` (`int`): How far, in degrees, you would like to rotate the object.
    * `origin` (`tuple`): A coordinate about which to rotate.
    '''
    if origin is None:
        # calculate reasonable origin
        top = get_top(canvas, tag)
        bottom = get_bottom(canvas, tag)
        left = get_left(canvas, tag)
        right = get_right(canvas, tag)
        origin = (right - left, bottom - top)

    degrees = math.radians(degrees)
    ox, oy = origin

    shape_ids = canvas.find_withtag(tag)
    for id in shape_ids:
        coords = _get_coordinates(canvas, id)
        # update coordinates:
        for i in range(0, len(coords), 2):
            px, py = coords[i], coords[i+1]
            qx = ox + math.cos(degrees) * (px - ox) - math.sin(degrees) * (py - oy)
            qy = oy + math.sin(degrees) * (px - ox) + math.cos(degrees) * (py - oy)
            coords[i] = qx
            coords[i+1] = qy
        # set the coordinates:
        _set_coordinates(canvas, id, coords)


def make_square(canvas, top_left, width, fill_color="green", tag=None, stroke_width=1, outline=None):
    '''
    Draws a square on a specified canvas with a particular corner coordinate.

    * `canvas` (`Canvas`): [Required] The `Canvas` to draw on.
    * `top_left` (`tuple`): [Required] A `(x,y)` coorindate marking the corner of the shape.
    * `width` (`float` or `int`): [Required] The width of the shape.
    * `fill_color` (`str`): Color name or hex code to fill the object with.
    * `tag` (`str`): The tag with which to name the object being drawn.
    * `stroke_width` (`int`): How wide to draw the outline of the shape.
    * `outline` (`str`): Color name or hex code used to outline the shape.

    Return an objectID `(int)`.
    '''
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + width)],
        fill=fill_color,
        tags=tag,
        width=stroke_width,
        outline=outline
    )

def make_rectangle(canvas, top_left, width, height, fill_color="black", tag=None, stroke_width=1, outline=None):
    '''
    Draws a square on a specified canvas with a particular `top_left` coordinate.

    * `canvas` (`Canvas`): [Required] The `Canvas` to draw on.
    * `top_left` (`tuple`): [Required] A `(x,y)` coorindate marking the corner of the shape.
    * `width` (`float` or `int`): [Required] The width of the shape.
    * `height` (`float` or `int`): [Required] The height of the shape.
    * `fill_color` (`str`): Color name or hex code to fill the object with.
    * `tag` (`str`): The tag with which to name the object being drawn.
    * `stroke_width` (`int`): How wide to draw the outline of the shape.
    * `outline` (`str`): Color name or hex code used to outline the shape.

    Return an objectID `(int)`.
    '''
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)],
        fill=fill_color,
        width=0,
        tags=tag
    )

def make_line(canvas, coordinates, curvy=False, fill_color="grey", width=2, tag=None, dash=None):
    '''
    Draws a line on a specified canvas between a list of coordinates.

    * `canvas` (`Canvas`): [Required] The `Canvas` to draw on.
    * `coordinates` (`list`): [Required] A list of coordinates with which to draw the line.
    * `smooth` (`bool`): Whether or not to curve the line through the specified coordinates.
    * `width` (`float` or `int`): The width of the line.
    * `fill_color` (`str`): Color name or hex code to fill the object with.
    * `tag` (`str`): The tag with which to name the object being drawn.
    * `dash` (`tuple`): Read more about the `dash` argument [here](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/dash-patterns.html).
   
    Return an objectID `(int)`.
    '''
    return canvas.create_line(
        coordinates,
        width=width,
        smooth=curvy,
        fill=fill_color,
        tag=tag,
        dash=None)

def get_left(canvas, tag):
    '''
    Returns the left-most x-coordinate of an object with the given tag.

    * `canvas` (`Canvas`): [Required] The `Canvas` to look at.
    * `tag` (`str`): [Required] The tag of the object to lookup.
    '''
    return min(*_get_x_coordinates(canvas, tag))

def get_right(canvas, tag):
    '''
    Returns the right-most x-coordinate of an object with the given tag.

    * `canvas` (`Canvas`): [Required] The `Canvas` to look at.
    * `tag` (`str`): [Required] The tag of the object to lookup.
    '''
    return max(*_get_x_coordinates(canvas, tag))

def get_top(canvas, tag):
    '''
    Returns the top-most y-coordinate of an object with the given tag.

    * `canvas` (`Canvas`): [Required] The `Canvas` to look at.
    * `tag` (`str`): [Required] The tag of the object to lookup.
    '''
    return min(*_get_y_coordinates(canvas, tag))

def get_bottom(canvas, tag):
    '''
    Returns the bottom-most y-coordinate of an object with the given tag.

    * `canvas` (`Canvas`): [Required] The `Canvas` to look at.
    * `tag` (`str`): [Required] The tag of the object to lookup.
    '''
    return max(*_get_y_coordinates(canvas, tag))

def get_width(canvas, tag):
    '''
    Returns the width of an object with the given tag.

    * `canvas` (`Canvas`): [Required] The `Canvas` to look at.
    * `tag` (`str`): [Required] The tag of the object to lookup.
    '''
    x_coords = _get_x_coordinates(canvas, tag)
    return max(*x_coords) - min(*x_coords)

def get_center(canvas, tag):
    '''
    Returns the center x-coordinate of an object with the given tag.

    * `canvas` (`Canvas`): [Required] The `Canvas` to look at.
    * `tag` (`str`): [Required] The tag of the object to lookup.
    '''

    return get_width(canvas, tag) / 2 + get_left(canvas, tag)

def get_height(canvas, tag):
    '''
    Returns the height of an object with the given tag.

    * `canvas` (`Canvas`): [Required] The `Canvas` to look at.
    * `tag` (`str`): [Required] The tag of the object to lookup.
    '''
    y_coords = _get_y_coordinates(canvas, tag)
    return max(*y_coords) - min(*y_coords)

def make_cloud(canvas, center, my_tag=""):
    '''
    Draws a weird looking cloud on a given `Canvas`

    * `canvas` (`Canvas`): [Required] The `Canvas` to drawn on.
    * `center` (`tuple`): [Required] A coordinate to center the cloud on.
    * `my_tag` (`str`): The tag to assign to the cloud.
    '''
    for i in range(random.randint(0,10)):
        x_offset = random.randint(-40,40)
        y_offset = random.randint(0,20)
        make_circle(canvas, (center[0] + x_offset, center[1] + y_offset), random.randint(10,50), tag=my_tag)

def make_car(canvas, top_left=(0, 0), fill_color="#3D9970", my_tag=None):
    '''
    Draws a cool car.

    * `canvas` (`Canvas`): [Required] The `Canvas` to draw on.
    * `top_left` (`tuple`): A coordinate at which to draw the car.
    * `fill_color` (`str`): Color name or hex code to fill the object with.
    * `my_tag` (`str`): The tag to assign to the car.

    '''
    x, y = top_left
    make_rectangle(canvas, (x + 50, y), 100, 40, fill_color=fill_color, tag=my_tag)
    make_rectangle(canvas, (x, y + 30), 200, 45, fill_color=fill_color, tag=my_tag)
    make_circle(canvas, (x + 50, y + 80), 20, fill_color='black', tag=my_tag)
    make_circle(canvas, (x + 150, y + 80), 20, fill_color='black', tag=my_tag)



def get_tag_from_event(canvas, event):
    '''
    Tries to return a tag of an object at a given mouse-event.

    * `canvas` (`Canvas`): [Required] The `Canvas` object to search in.
    * `event` (`Event`): [Required] Must be a mouse event otherwise we'll give back an error.
    '''
    try:

        x = event.x
        y = event.y
        shape_id = canvas.find_closest(x, y) # get the top shape
        if shape_id:
            tags = canvas.gettags(shape_id)
            if len(tags) > 0:
                # print(tags)
                return tags[0]
        return None
    except:
        print('error: none found')
        return None

def update_position(canvas, tag, x=0, y=0):
    '''
    Move a given tagged object on a particular canvas.

    * `canvas` (`Canvas`): [Required] The `Canvas` object to search in.
    * `tag` (`str`): [Required] The tag of the object to move.
    * `x` (`int`): A number of pixels to move in the x direction.
    * `y` (`int`): A number of pixels to move in the y direction.
    '''
    ids = canvas.find_withtag(tag)
    for id in ids:
        _update_position_by_id(canvas, id, x, y)

def update_fill(canvas, tag, color):
    '''
    Change the fill color of a tagged object.

    * `canvas` (`Canvas`): [Required] The `Canvas` object to search in.
    * `tag` (`str`): [Required] The tag of the object to re-fill.
    * `color` (`str`): [Required] A color name or hex code to re-fill with.
    '''
    ids = canvas.find_withtag(tag)
    for id in ids:
        canvas.itemconfig(id, fill=color)

def delete(canvas, tag):
    '''
    Delete a given tagged object on a particular canvas.

    * `canvas` (`Canvas`): [Required] The `Canvas` object to search in.
    * `tag` (`str`): [Required] The tag of the object to delete.

    Note, if an object doesn't exist with that tag, nothing will happen.
    '''
    ids = canvas.find_withtag(tag)
    for id in ids:
        canvas.delete(id)


def flip(canvas, tag):
    '''
    Flip across the vertical axis a given tagged object on a particular canvas.

    * `canvas` (`Canvas`): [Required] The `Canvas` object to search in.
    * `tag` (`str`): [Required] The tag of the object to flip.
    '''
    center = get_center(canvas, tag)
    width = get_width(canvas, tag)
    shape_ids = canvas.find_withtag(tag)
    for shape_id in shape_ids:
        flipped_coordinates = []
        shape_coords = _get_coordinates(canvas, shape_id)
        counter = 0
        for num in shape_coords:
            if counter % 2 == 0:
                if num < center:
                    flipped_coordinates.append(num + 2 * (center - num))
                elif num > center:
                    flipped_coordinates.append(num - 2 * (num - center))
                else:
                    flipped_coordinates.append(num)
            else:
                flipped_coordinates.append(num)
            counter += 1
        _set_coordinates(canvas, shape_id, flipped_coordinates)


def make_grid(canvas, width, height):
    '''
    Draw a grid on a given canvas.

    * `canvas` (`Canvas`): [Required] The `Canvas` object to drawn in.
    * `width` (`int`): [Required] Width of the grid to draw.
    * `height` (`int`): [Required] Height of the grid to draw.
    '''
    interval = 100

    # Delete old grid if it exists:
    canvas.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, width, interval):
        canvas.create_line(i, 0, i, height, tag='grid_line')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, height, interval):
            canvas.create_line(0, i, width, i, tag='grid_line')

            # Creates axis labels
            offset = 2
            for y in range(0, height, interval):
                for x in range(0, width, interval):
                    canvas.create_oval(
                    x - offset,
                    y - offset,
                    x + offset,
                    y + offset,
                    fill='black'
                    )
                    canvas.create_text(
                    x + offset,
                    y + offset,
                    text="({0}, {1})".format(x, y),
                    anchor="nw",
                    font=("Purisa", 8)
                    )
