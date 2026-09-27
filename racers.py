import turtle
colors=["blue","red","green","brown"]
def create_turtles():
    turtles=[]
    for color in colors:
        t=turtle.Turtle()
        t.shape("turtle")
        t.color(color)
        t.penup()
        turtles.append(t)
    return turtles

def setstarting(turtles):
    y=150
    for t in turtles:
        t.goto(-300,y)
        y=y-100




