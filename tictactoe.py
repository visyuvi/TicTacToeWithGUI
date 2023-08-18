from settings import *
import pygame as pg


class TicTacToe:
    def __init__(self, app):
        self.app = app
        self.markers = []
        self.create_markers()

    def draw_grid(self):
        for x in range(1,3):
            pg.draw.line(self.app.screen, GRID_COLOR, (0, x * 100), (FIELD_W, x * 100), LINE_WIDTH)
            pg.draw.line(self.app.screen, GRID_COLOR, (x * 100, 0), (x * 100, FIELD_H), LINE_WIDTH)

    def create_markers(self):
        for x in range(3):
            row = [0] * 3
            self.markers.append(row)

    def draw(self):
        self.draw_grid()

