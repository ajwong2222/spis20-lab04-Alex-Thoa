import turtle

def spiral(initial_length, angle, multiplier):
    spiralt.speed (1)
    if initial_length < 1:
        return
    else:       
        spiralt.pendown
        spiralt.forward (initial_length)
        spiralt.right (angle)
        spiral(initial_length * multiplier, angle, multiplier)

spiralt = turtle.Turtle()
spiral(100, 90, 0.9)

#Initial length is not less than one and so you move into else and carry out the movement in else. Line 11, call it again and go back to line three but our initial length underwent the change in line 11. Initial length is still not less than one and so it continues going to else and carrying out the action from line 11 to line 3 UNTIL initial length is less than 1. 