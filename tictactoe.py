import pygame.draw

from settings import *
import pygame as pg


class TicTacToe:
    def __init__(self, app):
        self.app = app
        self.markers = []
        self.create_markers()
        self.player = 1

    def draw_grid(self):
        for x in range(1,3):
            pg.draw.line(self.app.screen, GRID_COLOR, (0, x * 100), (FIELD_W, x * 100), LINE_WIDTH)
            pg.draw.line(self.app.screen, GRID_COLOR, (x * 100, 0), (x * 100, FIELD_H), LINE_WIDTH)

    def create_markers(self):
        for x in range(3):
            row = [0] * 3
            self.markers.append(row)

    def draw_markers(self):
        x_pos = 0
        for x in self.markers:
            y_pos = 0
            for y in x:
                if y == 1:
                    pg.draw.line(self.app.screen, GREEN, (x_pos * 100 + 15, y_pos * 100 + 15),
                                 (x_pos * 100 + 85, y_pos * 100 + 85), LINE_WIDTH)
                    pg.draw.line(self.app.screen, GREEN, (x_pos * 100 + 15, y_pos * 100 + 85),
                                 (x_pos * 100 + 85, y_pos * 100 + 15), LINE_WIDTH)
                if y == -1:
                    pg.draw.circle(self.app.screen, RED, (x_pos * 100 + 50, y_pos * 100 + 50), 38, LINE_WIDTH)
                y_pos += 1
            x_pos += 1

    def draw(self):
        self.draw_grid()
        self.draw_markers()

