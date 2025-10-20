import turtle
from itertools import cycle

screen = turtle.Screen()
screen.bgcolor('black')

t = turtle.Turtle()
t.speed('fastest')
t.width(2)

colors = ["red", "green", "blue"]


def draw_shape(turtle_obj, steps, length, turn_angle=None):
    """
    Draws a closed shape made of `steps` segments.
    - steps: number of line segments to draw (e.g. 5 for a pentagon/star pattern)
    - length: forward distance for each segment
    - turn_angle: degrees to turn after each segment. If None, uses regular polygon exterior angle (360/steps).
    """
    if turn_angle is None:
        turn = 360.0 / steps
    else:
        turn = turn_angle

    for _ in range(steps):
        turtle_obj.forward(length)
        turtle_obj.right(turn)


def draw_repeats(turtle_obj, steps, length, turn_angle, repeats, rotate_between):

    # Draw the same shape `repeats` times, rotating the turtle by `rotate_between` degrees between each draw.
    # controls how much the turtle turns before drawing the next polygon of the same color.
    
    for _ in range(repeats):
        draw_shape(turtle_obj, steps, length, turn_angle)
        turtle_obj.right(rotate_between)


# Example configuration: a list of shapes to draw for each color.
# Change `steps`, `length`, `turn` (optional), `repeats`, and `rotate_between` to experiment.
shapes = [
    # regular-ish 6-segment pattern (like your original)
    # {"steps": 6, "length": 100, "turn": 75, "repeats": 6, "rotate_between": 50},
    # a star / pentagon-like shape: 5 segments with a 144-degree turn makes a classic 5-point star
    # {"steps": 1, "length": 380, "turn": 144, "repeats": 18, "rotate_between": 15},
    # triangle pattern (regular triangle uses 120 exterior); small rotation between repeats
    {"steps": 3, "length": 155, "turn": None, "repeats": 15, "rotate_between": 112},
]


try:
    color_cycle = cycle(colors)
    for color in color_cycle:
        t.color(color)
        # draw each configured shape once in this color
        for cfg in shapes:
            draw_repeats(
                t,
                steps=cfg["steps"],
                length=cfg["length"],
                turn_angle=cfg["turn"],
                repeats=cfg["repeats"],
                rotate_between=cfg["rotate_between"],
            )
        # stop after cycling through all colors once
        # (break here prevents infinite loop from cycle())
        if color == colors[-1]:
            break
finally:
    t.hideturtle()
    turtle.done()