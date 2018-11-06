import turtle

window = turtle.Screen()

def draw(n):
    t = turtle.Turtle()
    length = (n + 1)*40
    for i in range(6):
        t.forward(length)
        t.right(180)
        t.forward(length)
        t.right(120)
    for i in range(n):
        t.forward(40)
        t.left(120)
        for j in range(6):
            t.forward((i + 1)*40)
            t.left(60)
        t.right(120)

draw(3)
