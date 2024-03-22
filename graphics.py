# graphics.py
from tkinter import Tk, BOTH, Canvas

class Window(Tk):
    def __init__(self, width, height):
        super().__init__()
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self, width=400, height=300)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.is_window_running = False

