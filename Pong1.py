# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')


# Paddle B

# Ball

# Main game loop
while True:
    wn.update()
