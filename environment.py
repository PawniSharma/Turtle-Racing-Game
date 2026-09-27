import turtle

#creating interface
def setup_screen():
    s=turtle.Screen()
    s.title("TURTLE RACING!")
    s.bgcolor("pink")
    return s

def draw_tracks():
    #finish line
    line=turtle.Turtle()
    line.penup()
    line.goto(280,200)
    line.pendown()
    line.goto(280,-200)
    line.hideturtle()

#starting line
    sline=turtle.Turtle()
    sline.penup()
    sline.goto(-320,200)
    sline.pendown()
    sline.goto(-320,-200)
    sline.hideturtle()


    #making tracks
    track=turtle.Turtle()
    track.speed(0)
    track.color("forestgreen")
    track.pensize(3)
    track.hideturtle()

    #makinglanes
    tracks=[200,100,0,-100,-200]
    for y in tracks:
        track.penup()
        track.goto(-320,y)
        track.pendown()
        track.goto(280,y)