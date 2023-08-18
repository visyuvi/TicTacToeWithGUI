import pygame.draw

from settings import *
import pygame as pg


class TicTacToe:
    def __init__(self, app):
        self.app = app
        self.markers = []
        self.create_markers()
        self.player = 1
        self.winner = 0
        self.game_over = False

    def draw_grid(self):
        for x in range(1, 3):
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

    def check_winner(self):
        y_pos = 0
        for x in self.markers:
            # check columns
            if sum(x) == 3:
                self.winner = 1
                self.game_over = True
            if sum(x) == -3:
                self.winner = 2
                self.game_over = True

            # check through the rows
            if self.markers[0][y_pos] + self.markers[1][y_pos] + self.markers[2][y_pos] == 3:
                self.winner = 1
                self.game_over = True
            if self.markers[0][y_pos] + self.markers[1][y_pos] + self.markers[2][y_pos] == -3:
                self.winner = 2
                self.game_over = True
            y_pos += 1

        # check cross
        if (self.markers[0][0] + self.markers[1][1] + self.markers[2][2] == 3) or \
                (self.markers[2][0] + self.markers[1][1] + self.markers[0][2] == 3):
            self.winner = 1
            self.game_over = True
        if (self.markers[0][0] + self.markers[1][1] + self.markers[2][2] == -3) or \
                (self.markers[2][0] + self.markers[1][1] + self.markers[0][2] == -3):
            self.winner = 2
            self.game_over = True

    def draw_winner(self):
        win_text = "Player " + str(self.winner) + "wins!"
        win_img = font.render(win_text, True, BLUE)
        pg.draw.rect(self.app.screen, GREEN,
                     (FIELD_W // 2 - win_img.get_width() // 2, FIELD_H // 2 - win_img.get_height() // 2 - 10,
                      win_img.get_width(), win_img.get_height() + 20))
        self.app.screen.blit(win_img,
                             (FIELD_W // 2 - win_img.get_width() // 2, (FIELD_H // 2 - win_img.get_height() // 2)))

    def draw(self):
        self.draw_grid()
        self.draw_markers()
