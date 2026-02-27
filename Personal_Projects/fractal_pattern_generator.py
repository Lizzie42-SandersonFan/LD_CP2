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
    def is_valid_hexa_code(string):
        hexa_code = re.compile(r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')
        return bool(re.match(hexa_code, string))
    
    def draw_fancy_triforce():
        pass
    
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
        color = input("Enter the hex code for the LINE color you would like (Ex: #FFFFFF, #000000, #1656AD):\n")
        if is_valid_hexa_code(color):
            # Valid color
            print("Yes")
            break
        else:
            print("Invalid input. Please try again")
            continue
    while True:
        back_color = input("Enter the hex code for the BACKGROUND color you would like (Ex: #FFFFFF, #000000, #1656AD):\n")
        if is_valid_hexa_code(back_color) and back_color != color:
            # Valid color
            print("Yes")
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

main()

# LOGIC FOR DRAWING FANCY TRIFORCE
# See fancy_triforce.png
# Am I drawing big triangle first or small triangles first?
    # small triangles first
# No ideas yet on what I would do if drawing small ones first