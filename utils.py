import turtle
from typing import Tuple

STATE_STACK = []
def save_current_state(turtle_: turtle.Turtle):
    angle, position = turtle_.heading(), turtle_.pos()
    STATE_STACK.append((angle, position))
    
def back_to_saved_state(turtle_: turtle.Turtle):
    angle, position = STATE_STACK.pop()
    turtle_.setheading(angle)
    turtle_.penup()
    turtle_.goto(position)
    turtle_.pendown()

def init_turtle(start_pos: Tuple[int, int], color: str, pen_size: int, speed: int, start_heading: float):
    turtle_ = turtle.Turtle()
    turtle_.pensize(pen_size)
    turtle_.speed(speed)
    turtle_.color(color)
    turtle_.setpos(*start_pos)
    turtle_.setheading(start_heading)
    
    return turtle_
