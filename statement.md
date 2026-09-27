# Problem Statement

## Problem Statement

A lot of the practice problems I'd worked through before this were just print statements and loops — you run the code and the "result" is a wall of text in a terminal. [I wanted to build something where I could actually watch my logic happen instead of just reading it.] Turtle graphics seemed like the easiest way to get something visual working without needing a whole game engine or new library to learn, so I built a small race sim around it — betting, randomness, input validation, and a results screen, all in one place.
## Objectives

- Build a small, working multi-file Python project instead of a single script
- Practice using the `turtle` module to create visual, animated output
- Implement a randomized simulation (the race) driven by the `random` module
- Take user input, validate it properly, and use it to affect the outcome shown to the user
- Get comfortable splitting logic across files and importing between them
- Add at least a basic test to check that core parts of the code work as expected

## Scope of the Project

This project is a small turtle-graphics based racing game built with Python. The scope is intentionally kept simple since this is my first multi-file project:

- Set up a race track with 4 lanes using the `turtle` module
- Create 4 turtles (blue, red, green, brown) that race by moving a random distance each round
- Let the user place a bet on which turtle will win before the race starts
- Validate the user's input so only valid colors are accepted
- Run the race until one turtle crosses the finish line
- Show the user whether they won or lost the bet
- Display a small analytics/report screen summarizing the race result

It does not include things like multiplayer, saving results between sessions, or a GUI beyond what turtle graphics provides - those are out of scope for now, though listed as possible future improvements in the README.

## Target Users

This project is aimed at:
- Beginner programmers (like myself) looking for a simple example of a multi-file Python project
- Anyone wanting a lightweight, visual way to see basic programming concepts (loops, functions, randomness, conditionals) in action
- Students/reviewers evaluating this as a course project, to see how the code is structured and how the game logic works

## Functional Requirements

1.Screen & Track Setup - a game window opens with 5 horizontal lanes and a marked start/finish line drawn using turtle.
2.Turtle Creation - 4 turtles (blue, red, green, brown) get created and placed at the starting line, one per lane.
3.Bet Input - before the race starts, the user is asked to type in the color they think will win.
4.Input Validation - blank input or anything outside the 4 valid colors gets rejected, and the prompt keeps repeating until a valid color comes in.
5.Race Simulation - each turtle moves forward by a random distance every round, so the race plays out differently each time.
6.Winner Detection - the moment a turtle's x-position crosses the finish line, its color is recorded as the winner.
7.Result Display - the user is told whether their bet matched the winner or not.
8.Analytics Report - after the race, a summary screen shows the winning color, the user's bet, and whether it was a hit or miss.
## High-Level Features

- Randomized turtle race simulation with 4 competitors
- User betting system with input validation
- Visual race track drawn using turtle graphics
- Win/loss result screen
- Post-race analytics report showing the winner, the user's bet, and the outcome
- Modular code structure split across separate files for setup, racers, UI text, and analytics
