import turtle

def write_title():
    title=turtle.Turtle()
    title.hideturtle()
    title.penup()
    title.color("red")
    title.goto(0,230)
    title.write("TURTLE RACING!",align="center",font=("Arial", 36, "bold"))

def display_winner(winner,bet):
        message=turtle.Turtle()
        message.hideturtle()
        message.penup()
        message.setheading(0)
        message.goto(0,-250)
        message.color("magenta")
        if winner==bet:
            message.write("You WON!    Winner: "+winner.upper(),align="center",font=("Arial",28,"bold"))

        else:
            message.write("You LOST!   Winner: "+winner.upper(),align="center",font=("Arial",28,"bold"))

