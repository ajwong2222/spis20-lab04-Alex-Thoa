import turtle
treet = turtle.Turtle()
treet.left (90)

def tree (trunk_length, height):
    if trunk_length < 1:
        return
    else :
        treet.speed(1)
        treet.pendown
        treet.forward (trunk_length)
        treet.left (45)
        tree (trunk_length // 2 , height - 1)
        treet.right (90)
        tree (trunk_length // 2 , height - 1)
        treet.left (45)
        treet.backward (trunk_length)

tree (100,4)