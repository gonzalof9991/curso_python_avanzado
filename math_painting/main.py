from canvas import Canvas
from shapes import Rectangle, Square

canvas_with = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))

# Make a dictionary of colors
colors = {"white": (255,255,255), "black": (0,0,0) }
canvas_color = input('Enter canvas color: (white or black) : ')


# Make a canvas
canvas = Canvas(height=canvas_height,width=canvas_with,color=colors[canvas_color])

while True:
    shape_type = input('Enter shape type (rectangle or square): ')
    # Ask for x and y
    if shape_type.lower() == 'rectangle':
        rec_x = int(input('Enter x: '))
        rec_y = int(input('Enter y: '))
        rec_width = int(input('Enter width: '))
        rec_height = int(input('Enter height: '))
        red = int(input('Enter red: '))
        green = int(input('Enter green: '))
        blue = int(input('Enter blue: '))

        # Create the rectangle
        r1 = Rectangle(x=rec_x,y=rec_y, height=rec_height, width=rec_width,color=(red,green,blue))
        # Draw the rectangle
        r1.draw(canvas)
    
    elif shape_type.lower() == 'square':
        sq_x = int(input('Enter x: '))
        sq_y = int(input('Enter y: '))
        sq_side = int(input('Enter side: '))
        red = int(input('Enter red: '))
        green = int(input('Enter green: '))
        blue = int(input('Enter blue: '))

        # Create the rectangle
        s1 = Square(x=sq_x,y=sq_y, side=sq_side,color=(red,green,blue))
        # Draw the rectangle
        s1.draw(canvas)
    
    if input('Do you want to continue? (y/n) ') == 'n':
        break

# Save the canvas
canvas.make('canvas.png')
