# LD 1st Fractal Pattern Generator
import turtle
import re

# Create a Python program that generates a Sierpinski Triangle fractal pattern using recursion. The program should allow users to customize the recursion depth and color of the fractal.

# STEPS
# Implement a main function that runs the program and handles user input
# Create a function to draw the Sierpinski Triangle using recursion
# Use Python's turtle graphics module for drawing
# Allow users to specify:
    # Recursion depth (1-5)
    # Triangle color
# HINT: Remember to implement a base case in your recursive function to prevent infinite recursion!

# EXTRA CREDIT
# Allow the user to save the generated fractal as an image file (3 points)
# Add an option to change the background color (1 point)

def main():
    turtle = turtle.Turtle()

    def is_valid_hexa_code(string):
        hexa_code = re.compile(r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')
        return bool(re.match(hexa_code, string))

    def get_midpoint(point1, point2):
        return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)
    
    def draw_fancy_triforce(position):
        nonlocal turtle
        turtle.up()
        turtle.goto(position[0][0], position[0][1])
        turtle.down()
        turtle.goto(position[1][0], position[1][1])
        turtle.goto(position[2][0], position[2][1])
        turtle.goto(position[0][0], position[0][1])

    def recursive_draw(turt, tri_num, point):
        draw_fancy_triforce(point)
        if tri_num > 0:
            recursive_draw(turt, tri_num-1, [p[0], get_midpoint(p[0], p[1]), get_midpoint(p[0], p[2])])
            recursive_draw(turt, tri_num-1, [p[1], get_midpoint(p[0], p[1]), get_midpoint(p[1], p[2])])
            recursive_draw(turt, tri_num-1, [p[2], get_midpoint(p[2], p[1]), get_midpoint(p[0], p[2])])
        else:
            return 0
    
    start_point = [[-500, -400], [0, 500], [500, -400]]
    # Greet user
    while True:
        depth = input("Enter Recursion Depth for your Triangle (1-5):\n")
        if depth == "1" or depth == "2" or depth == "3" or depth == "4" or depth == "5":
            # Valid input
            depth = int(depth)
            break
        else:
            print("Invalid input. Try again")
            continue
    while True:
        pen_color = input("Enter the hex code for the LINE color you would like (Ex: #FFFFFF, #000000, #1656AD):\n")
        if is_valid_hexa_code(pen_color):
            # Valid color
            break
        else:
            print("Invalid input. Please try again")
            continue
    while True:
        back_color = input("Enter the hex code for the BACKGROUND color you would like (Ex: #FFFFFF, #000000, #1656AD):\n")
        if is_valid_hexa_code(back_color) and back_color != color:
            # Valid color
            break
        else:
            if is_valid_hexa_code(back_color) == False:
                print("Invalid color. Try again")
                continue
            elif back_color == color:
                print("Your background color cannot be the same as your lines. Pick a different color")
                continue
            else:
                print("What in world happened!?!?")

    # Set up turtle colors and start drawing!
    turtle.hideturtle()
    turtle.pencolor(pen_color)
    turtle.bgcolor(back_color)
    recursive_draw(turtle, 5, start_point)
    turtle.done()
    # Now figure out how the user can save it as an image

main()