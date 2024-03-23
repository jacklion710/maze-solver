# maze.py
from cell import Cell
from queue import PriorityQueue, Queue
import random
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visted()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visted(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _solve_dfs(self, i, j, color):
        stack = [(i, j)]
        came_from = {}
        came_from[(i, j)] = None

        while stack:
            current = stack.pop()
            i, j = current

            if i == self._num_cols - 1 and j == self._num_rows - 1:
                break

            for next_cell in self._get_neighbors(i, j):
                if next_cell not in came_from:
                    stack.append(next_cell)
                    came_from[next_cell] = current

        if (self._num_cols - 1, self._num_rows - 1) not in came_from:
            return False

        self._draw_path(came_from, color)
        return True

    def _solve_bfs(self, i, j, color):
        queue = Queue()
        queue.put((i, j))
        came_from = {}
        came_from[(i, j)] = None

        while not queue.empty():
            current = queue.get()
            i, j = current

            if i == self._num_cols - 1 and j == self._num_rows - 1:
                break

            for next_cell in self._get_neighbors(i, j):
                if next_cell not in came_from:
                    queue.put(next_cell)
                    came_from[next_cell] = current

        if (self._num_cols - 1, self._num_rows - 1) not in came_from:
            return False

        self._draw_path(came_from, color)
        return True

    def _solve_dijkstra(self, i, j, color):
        pq = PriorityQueue()
        pq.put((0, (i, j)))
        came_from = {}
        cost_so_far = {}
        came_from[(i, j)] = None
        cost_so_far[(i, j)] = 0

        while not pq.empty():
            _, current = pq.get()
            i, j = current

            if i == self._num_cols - 1 and j == self._num_rows - 1:
                break

            for next_cell in self._get_neighbors(i, j):
                new_cost = cost_so_far[(i, j)] + 1
                if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                    cost_so_far[next_cell] = new_cost
                    pq.put((new_cost, next_cell))
                    came_from[next_cell] = current

        if (self._num_cols - 1, self._num_rows - 1) not in came_from:
            return False

        self._draw_path(came_from, color)
        return True
    
    def _solve_astar(self, i, j, color):
        self._animate()

        pq = PriorityQueue()
        pq.put((0, (i, j)))
        came_from = {}
        cost_so_far = {}
        came_from[(i, j)] = None
        cost_so_far[(i, j)] = 0

        while not pq.empty():
            _, current = pq.get()
            i, j = current

            if i == self._num_cols - 1 and j == self._num_rows - 1:
                break

            for next_cell in self._get_neighbors(i, j):
                new_cost = cost_so_far[(i, j)] + 1
                if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                    cost_so_far[next_cell] = new_cost
                    priority = new_cost + self._heuristic(next_cell[0], next_cell[1])
                    pq.put((priority, next_cell))
                    came_from[next_cell] = (i, j)

        if (self._num_cols - 1, self._num_rows - 1) not in came_from:
            return False

        self._draw_path(came_from, color)
        return True

    def _get_neighbors(self, i, j):
        neighbors = []

        if i > 0 and not self._cells[i][j].has_left_wall:
            neighbors.append((i - 1, j))
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall:
            neighbors.append((i + 1, j))
        if j > 0 and not self._cells[i][j].has_top_wall:
            neighbors.append((i, j - 1))
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall:
            neighbors.append((i, j + 1))

        return neighbors

    def _heuristic(self, i, j):
        return abs(i - (self._num_cols - 1)) + abs(j - (self._num_rows - 1))

    def _draw_path(self, came_from, color):
        current = (self._num_cols - 1, self._num_rows - 1)
        while current != (0, 0):
            i, j = current
            self._cells[i][j].visited = True
            next_cell = came_from[current]
            if next_cell is not None:
                self._cells[i][j].draw_move(self._cells[next_cell[0]][next_cell[1]], color)
            current = next_cell

    def solve(self):
        algorithms = [
            ('DFS', self._solve_dfs, 'red'),
            ('BFS', self._solve_bfs, 'green'),
            ('Dijkstra', self._solve_dijkstra, 'blue'),
            ('A*', self._solve_astar, 'orange')
        ]

        results = []
        for name, algorithm, color in algorithms:
            self._reset_cells_visted()
            start_time = time.time()
            is_solvable = algorithm(0, 0, color)
            end_time = time.time()
            results.append((name, is_solvable, end_time - start_time))

        return results
