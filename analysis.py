import turtle

def gamereport(screen, color, bet):
    screen.clear()
    screen.bgcolor("cyan") 
    
    
    report = turtle.Turtle()
    report.hideturtle()
    report.penup()
    report.color("brown")
    
    # Heading
    report.goto(0, 80)
    report.write("_________________________", align="center", font=("Arial", 18, "bold"))
    report.goto(0, 50)
    report.write("      RACE ANALYTICS     ", align="center", font=("Arial", 20, "bold"))
    report.goto(0, 30)
    report.write("_________________________", align="center", font=("Arial", 18, "bold"))
    
    #Stats
    report.color("green")
    report.goto(0, -20)
    report.write("Winning Turtle Color : " + str(color).upper(), align="center", font=("Arial", 16, "normal"))
    report.color("blue")
    report.goto(0, -60)
    report.write("Your Predicted Bet   : " + str(bet).upper(), align="center", font=("Arial", 16, "normal"))
    
    # Checking output vs bet
    report.color("red")
    report.goto(0, -110)
    if color == bet:
        report.write("Result Summary  : SUCCESS (Bet Matched)", align="center", font=("Arial", 16, "bold"))
    else:
        report.write("Result Summary  : FAILURE (Bet Mis-matched)", align="center", font=("Arial", 16, "normal"))
        
    report.goto(0, -150)
    report.write("__________________________", align="center", font=("Arial", 18, "bold"))
