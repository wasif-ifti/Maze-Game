# room.py
# Name: Wasif Islam
# Description: A room in the maze. Like a linked list node, but with
#              four "next" pointers (north, south, east, west) instead of one.


class Room:
    # Every door starts closed (None) until it's linked to another room
    def __init__(self, descr):
        self.__description = descr
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None

    def __str__(self):
        return self.__description

    # Accessors
    def getNorth(self):
        return self.__north

    def getSouth(self):
        return self.__south

    def getEast(self):
        return self.__east

    def getWest(self):
        return self.__west

    def getExits(self):
        """Return the list of directions that lead somewhere."""
        exits = []
        if self.__north is not None:
            exits.append("north")
        if self.__south is not None:
            exits.append("south")
        if self.__east is not None:
            exits.append("east")
        if self.__west is not None:
            exits.append("west")
        return exits

    # Mutators
    def setDescription(self, d):
        self.__description = d

    def setNorth(self, n):
        self.__north = n

    def setSouth(self, s):
        self.__south = s

    def setEast(self, e):
        self.__east = e

    def setWest(self, w):
        self.__west = w


def connect(a, direction, b):
    """Link room a to room b in a direction, and b back to a the opposite way."""
    if direction == "north":
        a.setNorth(b)
        b.setSouth(a)
    elif direction == "south":
        a.setSouth(b)
        b.setNorth(a)
    elif direction == "east":
        a.setEast(b)
        b.setWest(a)
    elif direction == "west":
        a.setWest(b)
        b.setEast(a)
