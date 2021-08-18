#this code does not work as a sierpinski triangle, but I understand recursions better having looked at it. 
import turtle
trianglet = turtle.Turtle()
trianglet.speed (10)
def triangle (length, level):
    if level < 1:
            trianglet.forward(length)
            trianglet.left(120)
 
    else:
        trianglet.forward (length // 2)
        trianglet.left (120)
        trianglet.forward (length //2)
        trianglet.left (120)
        trianglet.forward (length //2)
        trianglet.left (120)
        trianglet.forward (length)
        trianglet.left (120)
        trianglet.forward (length //2)
        trianglet.left (120)
        trianglet.forward (length //2)
        trianglet.left (120)        
        triangle(length//2, level - 1 )


triangle (100,3)