# Design Documentation

This file contains the system architecture, workflow, use case diagram, and non-functional requirements for the Turtle Racing Game project.

## Non-Functional Requirements

- **Usability** - the game gives clear on-screen prompts (e.g. "Which Turtle will win the race?") and re-asks the question if an invalid color is entered, so the user always knows what to do next.
- **Reliability** - the input validation loop in `main.py` makes sure the game never crashes or breaks due to bad user input; it just keeps asking until a valid color is given.
- **Maintainability** - the code is split into 6 separate files by responsibility (setup, racers, UI text, analysis, testing), so a bug or change in one part (e.g. track drawing) doesn't require touching unrelated files.
- **Performance** - the race loop uses small random increments per frame so the animation runs smoothly without noticeable lag on a normal machine.
- **Resource efficiency** - the game only uses built-in Python libraries (`turtle`, `random`), so there's no extra memory/dependency overhead from external packages.

## System Architecture Diagram

```mermaid
graph TD
    A[main.py] --> B[environment.py]
    A --> C[racers.py]
    A --> D[ui_text.py]
    A --> E[analysis.py]
    F[verifytest.py] --> C

    B -->|setup_screen, draw_tracks| A
    C -->|create_turtles, setstarting| A
    D -->|write_title, display_winner| A
    E -->|gamereport| A
```

**Explanation:** `main.py` is the entry point that ties every module together. `environment.py` handles the screen and track visuals, `racers.py` handles turtle creation and starting positions, `ui_text.py` handles the title and win/lose message, and `analysis.py` generates the post-race report. `verifytest.py` is a standalone test file that imports `racers.py` to verify turtle creation independently of the game loop.


## Process Flow / Workflow Diagram

```mermaid
flowchart TD
    Start([Start Game]) --> Setup[Setup screen & draw tracks]
    Setup --> CreateTurtles[Create 4 turtles]
    CreateTurtles --> Position[Place turtles at starting line]
    Position --> Bet{Ask user for bet}
    Bet -->|Invalid color| Bet
    Bet -->|Valid color| Race[Start race loop]
    Race --> Move[Move each turtle by random distance]
    Move --> Check{Has a turtle crossed finish line?}
    Check -->|No| Move
    Check -->|Yes| Winner[Determine winner]
    Winner --> Display[Show Win/Loss message]
    Display --> Report[Show race analytics report]
    Report --> End([End])
```

## Use Case Diagram

```mermaid
graph LR
    User((User))
    User --> UC1[Enter bet / color prediction]
    User --> UC2[Watch race animation]
    User --> UC3[View win/loss result]
    User --> UC4[View race analytics report]

    System((Turtle Racing System))
    UC1 --> System
    UC2 --> System
    UC3 --> System
    UC4 --> System
```

**Explanation:** The only actor in this system is the User. They interact with the system by placing a bet, watching the race, and then viewing the outcome and analytics. There's no admin/second actor since this is a single-player local game.


## Sequence Diagram (Race Flow)

```mermaid
sequenceDiagram
    participant U as User
    participant M as main.py
    participant E as environment.py
    participant R as racers.py
    participant A as analysis.py

    U->>M: Run program
    M->>E: setup_screen()
    M->>R: create_turtles()
    M->>E: draw_tracks()
    M->>U: Ask for bet
    U->>M: Enter color
    loop Until turtle crosses finish line
        M->>R: move turtle forward(random distance)
    end
    M->>A: gamereport(winner, bet)
    A->>U: Display analytics report
```

## Notes

These diagrams are written in Mermaid syntax, which GitHub renders automatically when viewing the `.md` file in your repository - no extra image files needed. If your report PDF needs static images instead of code blocks, you can paste this Mermaid code into the [Mermaid Live Editor](https://mermaid.live) and export as PNG/SVG.
