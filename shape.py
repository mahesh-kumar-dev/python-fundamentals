import turtle

# 1. Set up the screen and turtle
screen = turtle.Screen()
screen.title("VS Code Turtle Test")
my_turtle = turtle.Turtle()

# 2. Draw a simple square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

# 3. CRITICAL: Keeps the GUI window open in VS Code
turtle.done()
