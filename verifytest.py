# Simple functional testing suite required by the project guidelines
import racers

def test_turtle_count():
    print("Initializing test check...")
    test_list = racers.create_turtles()
    # Check if exactly 4 turtles are created as expected
    if len(test_list) == 4:
        print("SUCCESS: 4 dynamic turtle entities generated.")
    else:
        print("FAILURE: Turtle list count incorrect.")

def test_color_list():
    # colors list should have exactly the 4 racing colors, no duplicates
    if len(racers.colors) == 4 and len(set(racers.colors)) == 4:
        print("SUCCESS: colors list has 4 unique colors.")
    else:
        print("FAILURE: colors list is wrong or has duplicates.")

def test_turtle_colors_match():
    # each created turtle's color should actually be one of the defined colors
    test_list = racers.create_turtles()
    all_match = True
    for t in test_list:
        if t.color()[0] not in racers.colors:
            all_match = False
    if all_match:
        print("SUCCESS: all turtle colors match the defined colors list.")
    else:
        print("FAILURE: some turtle got an unexpected color.")

def test_starting_positions():
    # starting positions should be different for each turtle (no overlap)
    test_list = racers.create_turtles()
    racers.setstarting(test_list)
    y_positions = [t.ycor() for t in test_list]
    if len(set(y_positions)) == len(y_positions):
        print("SUCCESS: turtles placed at distinct starting lanes.")
    else:
        print("FAILURE: two or more turtles share the same lane.")

if __name__ == "__main__":
    test_turtle_count()
    test_color_list()
    test_turtle_colors_match()
    test_starting_positions()