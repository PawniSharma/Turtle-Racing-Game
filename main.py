import turtle
import random

# Import other modules
import environment
import ui_text
import racers
import analysis


s = environment.setup_screen()
turtles = racers.create_turtles()

# titlewriting
ui_text.write_title()

# startingposition
racers.setstarting(turtles)

# drawinglanes
environment.draw_tracks()

# asking user to bet
bet = s.textinput(title="Make yor bet!", prompt="Which Turtle will win the race? Enter a colour:")
while bet is None or bet.strip().lower() not in racers.colors:
    bet = s.textinput(title="Invalid entry", prompt="Please enter a valid colour (blue/red/green/brown):")
bet = bet.strip().lower()

# racing loop 
winner = ""
while winner == "":
    for t in turtles:
        distance = random.randint(1, 10)
        t.forward(distance)
        if t.xcor() >= 250:
            winner = t.color()[0]
            break

# displaying the winner
ui_text.display_winner(winner, bet)

#analysis
analysis.gamereport(s,winner, bet)


turtle.done()