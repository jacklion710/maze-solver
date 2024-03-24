# Maze Solver

This is a guided project from [boot.dev](https://boot.dev) that focuses on solving mazes using different search algorithms. The project demonstrates the implementation and visualization of Depth-First Search (DFS), Breadth-First Search (BFS), Dijkstra's algorithm, and A* search algorithm in Python.

## Features

- Generates a random maze with a specified number of rows and columns
- Solves the maze using DFS, BFS, Dijkstra's algorithm, and A* search algorithm
- Visualizes the maze and the paths taken by each algorithm using a graphical user interface (GUI)
- Displays the time taken by each algorithm to solve the maze
- Ensures that each run generates a completely different maze
- Illustrates the paths tried but not taken by each algorithm in a slightly less opaque color

## Requirements

- Python 3.x
- tkinter library (usually comes pre-installed with Python)

## Installation

1. Clone the repository:

  ```bash
  git clone https://github.com/yourusername/maze-solver.git
```

Navigate to the project directory:

```bash
cd maze-solver
```

Run the main.py script:

```bash
python main.py
```

## Usage

Upon running the `main.py` script, a window will open displaying the generated maze. The script will then solve the maze using DFS, BFS, Dijkstra's algorithm, and A* search algorithm. The paths taken by each algorithm will be visualized in different colors, and the time taken by each algorithm to solve the maze will be displayed in the console and the GUI.

The paths tried but not taken by each algorithm will be illustrated in a slightly less opaque variation of each path's color.

Each time the script is run, a completely different maze will be generated, ensuring a unique experience for each execution.

Project Structure
The project consists of the following files:

* `main.py`: The main script that generates the maze, solves it using different algorithms, and visualizes the results.
* `maze.py`: Contains the `Maze` class, which represents the maze and provides methods for generating and solving the maze.
* `cell.py`: Contains the `Cell` class, which represents a single cell in the maze and provides methods for drawing the cell and its walls.
* `graphics.py`: Contains the `Window` class, which creates the GUI window and provides methods for drawing lines and text.

Acknowledgements
boot.dev for providing the guided project and inspiration.
Tkinter library for creating the GUI.