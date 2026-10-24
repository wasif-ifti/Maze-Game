# 🏚️ Maze Game

> 🎓 Made during Lab 7 for **CS 172** at **Drexel University**

**[▶️ Play it in your browser](https://wasif-ifti.github.io/Maze-Game/)**

A text adventure where you type directions to find your way out of a maze. Pick one of three mazes, including **The Old Mansion**, a 9-room haunted house with dead ends, a loop, and a garden somewhere to the north.

## The idea

This started as a linked list lab. A linked list node has one `next` pointer. Here, every **room** is a node with **four** pointers (north, south, east, west), and moving through the maze is just following those pointers from room to room.

| Linked list | Maze game |
|---|---|
| `Node` | `Room` |
| `next` | `north` / `south` / `east` / `west` |
| `head` | start room |
| a "current" pointer | the room the player is in |

## Features

- **3 mazes:** Simple (3 rooms), Intermediate (6 rooms), and The Old Mansion (9 rooms)
- **Exit hints:** every room lists which directions are open
- **Move counter:** see how fast you can escape
- **Restart:** type `restart` to go back to the start

## Sample run

```
=== The Old Mansion ===

The Foyer. Dusty coats hang by the front door, which is locked behind you.
Exits: north, east, west
Which way? (north/south/east/west, or restart) north
You went north.

The Hallway. Portraits on the walls seem to follow you with their eyes.
Exits: north, south, east, west
...
The Garden. Fresh air at last!
You found the exit in 4 moves!
```

## How it's built

- **`room.py`**: the `Room` class (a node with four door pointers) plus a `connect()` helper that links two rooms both ways at once
- **`maze.py`**: the `Maze` class, which tracks the start, the exit, the current room, and the move count
- **`main.py`**: builds the three mazes and runs the game loop

## Run it

```bash
python main.py
```

No extra libraries needed.

## Built with

Python · classes · linked structures
