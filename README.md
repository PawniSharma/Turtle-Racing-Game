# Turtle Racing Game 

This is my project for the course - a simple turtle racing game made using Python's `turtle` module. You pick a color, the turtles race, and it tells you if you won or lost along with a small analytics screen.

I made this as my first proper multi-file Python project, so it's not super advanced, but I tried to keep the code organized instead of dumping everything into one file.

## Overview

The game sets up a race track with 4 lanes (blue, red, green, brown turtles). You place a bet on which color will win before the race starts. Once the race begins, each turtle moves forward by a random distance every round until one of them crosses the finish line. After the race, it shows whether your bet was correct and gives a small "analytics" screen summarizing the result.

Basically I wanted to practice:
- working with multiple files and importing between them
- using loops and conditionals for game logic
- taking and validating user input
- turtle graphics for a bit of visual output instead of just print statements

## Features

- Randomized turtle race (4 turtles, 4 colors)
- User can bet on a color before the race starts
- Input validation - keeps asking until you type a valid color
- Live race animation using turtle graphics
- Win/Loss message after the race
- A simple "Race Analytics" report screen showing winner, your bet, and result

## Technologies / Tools Used

- Python 3
- `turtle` module (built-in, comes with Python)
- `random` module (built-in)

No external libraries needed, everything runs with a normal Python install.

## Project Structure

```
├── main.py          # runs the whole game, ties everything together
├── environment.py   # sets up the screen and draws the race track
├── racers.py        # creates the turtles and sets their starting positions
├── ui_text.py       # handles title text and win/lose message
├── analysis.py      # shows the analytics/report screen after the race
├── verifytest.py    # basic test to check turtles are being created correctly
```

I split it this way because it felt easier to debug - if something's wrong with the track it's obviously in `environment.py`, if the race logic is off it's in `main.py`, etc.

## How to Install & Run

1. Make sure you have Python 3 installed (turtle comes bundled with it, no pip install needed).
2. Download/clone this repo.
3. Open a terminal in the project folder.
4. Run:
   ```
   python main.py
   ```
5. A window will pop up - type in a color (blue/red/green/brown) when it asks for your bet, and watch the race.

## Testing

There's a basic test file `verifytest.py` that checks that exactly 4 turtle objects get created by `racers.create_turtles()`. To run it:

```
python verifytest.py
```

It's not a huge test suite since most of the "logic" here is visual (turtle movement), but it covers the core data setup part which is the easiest thing to actually verify.

## Known limitations / things I'd improve later

- Right now there's no way to restart the race without closing and reopening the window
- Would be nice to add a scoreboard that tracks wins across multiple races
- Turtle speed is fixed, could add a difficulty/speed setting

## Screenshots
![alt text](image.png)
![alt text](image-1.png)