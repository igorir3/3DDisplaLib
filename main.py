import pygame

class window():
    def __init__(self, x_in:int, y_in:int, x_window_in:int,
                 y_window_in:int, size_window_in:tuple, 
                 demmatrix_in:list, lastpositions_in:bool,
                 coloroflastpositions_in:tuple, rotate_in:str) -> None:
        self.x = x_in
        self.y = y_in
        self.x_window = x_window_in
        self.y_window = y_window_in
        self.size_window = size_window_in
        self.modificator = [x_window_in / size_window_in[0], y_window_in / size_window_in[1]]
        self.demmatrix = demmatrix_in
        self.lastpositions = lastpositions_in
        self.coloroflastpositions = coloroflastpositions_in
        self.rotate = rotate_in.lower()
        if self.rotate != "front" and self.rotate != "back" and self.rotate != "left" and self.rotate != "right" and self.rotate != "up" and self.rotate != "down":
            raise SystemError(f"Не известная сторона: {self.rotate}")

    def init_window():
        pygame.init()

    def change_rotate(self, rotate_in:str):
        self.rotate = rotate_in

    def change_size(self, x_window_in:int, y_window_in:int):
        self.x_window = x_window_in
        self.y_window = y_window_in
        self.modificator = [x_window_in / self.size_window[0], y_window_in / self.size_window[1]]

    def update(self, matrix_in):
        pass

