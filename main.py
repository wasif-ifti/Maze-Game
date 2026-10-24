# main.py
# Name: Wasif Islam
# Description: Text-based maze game. Pick a maze, then type directions
#              until you find the exit.

from room import Room, connect
from maze import Maze


def buildSimpleMaze():
    # Solved by going east, then north
    #             [Room2] (exit)
    #                |
    #   [Room1] - [Room3]
    #   (start)
    room1 = Room("Room1")
    room2 = Room("Room2")
    room3 = Room("Room3")
    connect(room1, "east", room3)
    connect(room3, "north", room2)
    return Maze("Simple Maze", room1, room2)


def buildIntermediateMaze():
    # Solved by going west, west, west, north, east
    r1 = Room("Room1")
    r2 = Room("Room2")
    r3 = Room("Room3")
    r4 = Room("Room4")
    r5 = Room("Room5")
    r6 = Room("Room6")
    connect(r1, "west", r2)
    connect(r2, "west", r3)
    connect(r3, "west", r4)
    connect(r4, "north", r5)
    connect(r5, "east", r6)
    return Maze("Intermediate Maze", r1, r6)


def buildMansionMaze():
    # A bigger maze with dead ends and a loop.
    #
    #                        [Garden] (exit)
    #                           |
    #              [Ballroom]-[Study]
    #                  |         |
    #   [Kitchen] - [Hallway] - [Library]
    #       |           |
    #   [Dining] -- [Foyer] -- [Sitting Room]
    #                (start)
    foyer = Room("The Foyer. Dusty coats hang by the front door, which is locked behind you.")
    dining = Room("The Dining Hall. A long table is still set for a dinner nobody ate.")
    sitting = Room("The Sitting Room. Old armchairs face a cold fireplace. Dead end.")
    kitchen = Room("The Kitchen. Something is bubbling on the stove... best not to ask.")
    hallway = Room("The Hallway. Portraits on the walls seem to follow you with their eyes.")
    library = Room("The Library. Shelves of books stretch up into the dark.")
    ballroom = Room("The Ballroom. A cracked chandelier sways even though there's no wind.")
    study = Room("The Study. A desk covered in maps. One shows a garden to the north.")
    garden = Room("The Garden. Fresh air at last!")

    connect(foyer, "west", dining)
    connect(foyer, "east", sitting)
    connect(foyer, "north", hallway)
    connect(dining, "north", kitchen)
    connect(kitchen, "east", hallway)
    connect(hallway, "east", library)
    connect(hallway, "north", ballroom)
    connect(library, "north", study)
    connect(ballroom, "east", study)
    connect(study, "north", garden)
    return Maze("The Old Mansion", foyer, garden)


def play(myMaze):
    """Prompt for directions until the player finds the exit."""
    print("\n=== " + myMaze.getName() + " ===")
    while not myMaze.atExit():
        room = myMaze.getCurrent()
        print("\n" + str(room))
        print("Exits: " + ", ".join(room.getExits()))

        direction = input("Which way? (north/south/east/west, or restart) ").strip().lower()

        if direction == "north":
            myMaze.moveNorth()
        elif direction == "south":
            myMaze.moveSouth()
        elif direction == "east":
            myMaze.moveEast()
        elif direction == "west":
            myMaze.moveWest()
        elif direction == "restart" or direction == "reset":
            myMaze.reset()
        else:
            print("Direction invalid, try again.")

    print("\n" + str(myMaze.getCurrent()))
    print("You found the exit in " + str(myMaze.getMoves()) + " moves!")


def main():
    print("Welcome to the Maze Game!")
    print("1. Simple Maze")
    print("2. Intermediate Maze")
    print("3. The Old Mansion")
    choice = input("Pick a maze (1-3): ").strip()

    if choice == "1":
        play(buildSimpleMaze())
    elif choice == "2":
        play(buildIntermediateMaze())
    else:
        play(buildMansionMaze())


if __name__ == "__main__":
    main()
