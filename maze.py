# maze.py
# Name: Wasif Islam
# Description: Tracks the start room, the exit room, and where the player is.
#              Like a linked list that remembers its head and a "current" pointer.


class Maze:
    def __init__(self, name, st=None, ex=None):
        self.__name = name
        self.__start = st      # Room the player starts in
        self.__exit = ex       # Find this room to win
        self.__current = st    # Room the player is in right now
        self.__moves = 0

    def getName(self):
        return self.__name

    def getCurrent(self):
        return self.__current

    def getMoves(self):
        return self.__moves

    def __move(self, nextRoom, direction):
        # Shared logic for all four directions
        if nextRoom is None:
            print("You can't go " + direction + " from here.")
            return False
        self.__current = nextRoom
        self.__moves += 1
        print("You went " + direction + ".")
        return True

    def moveNorth(self):
        return self.__move(self.__current.getNorth(), "north")

    def moveSouth(self):
        return self.__move(self.__current.getSouth(), "south")

    def moveEast(self):
        return self.__move(self.__current.getEast(), "east")

    def moveWest(self):
        return self.__move(self.__current.getWest(), "west")

    def atExit(self):
        return self.__current == self.__exit

    def reset(self):
        self.__current = self.__start
        self.__moves = 0
        print("You went back to the start!")
