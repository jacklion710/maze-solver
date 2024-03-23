# cell.py
from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, color, offset, undo=False):
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1 + offset, y_mid + offset), Point(x_mid + offset, y_mid + offset))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid + offset, to_y_mid + offset), Point(to_cell._x2 + offset, to_y_mid + offset))
            self._win.draw_line(line, color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid + offset, y_mid + offset), Point(self._x2 + offset, y_mid + offset))
            self._win.draw_line(line, color)
            line = Line(Point(to_cell._x1 + offset, to_y_mid + offset), Point(to_x_mid + offset, to_y_mid + offset))
            self._win.draw_line(line, color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid + offset, y_mid + offset), Point(x_mid + offset, self._y1 + offset))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid + offset, to_cell._y2 + offset), Point(to_x_mid + offset, to_y_mid + offset))
            self._win.draw_line(line, color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid + offset, y_mid + offset), Point(x_mid + offset, self._y2 + offset))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid + offset, to_y_mid + offset), Point(to_x_mid + offset, to_cell._y1 + offset))
            self._win.draw_line(line, color)
