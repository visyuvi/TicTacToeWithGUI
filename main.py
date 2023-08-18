from settings import *
import sys
import pygame as pg
from tictactoe import *
pg.init()


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('TicTacToe')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.tictactoe = TicTacToe(self)
        self.tictactoe.player = 1
        self.clicked = False

    def update(self):
        self.clock.tick(FPS)
        pg.display.update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.tictactoe.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if not self.tictactoe.game_over:
                if event.type == pg.MOUSEBUTTONDOWN and not self.clicked:
                    self.clicked = True
                if event.type == pg.MOUSEBUTTONUP and self.clicked:
                    self.clicked = False
                    POS = pg.mouse.get_pos()
                    cell_x = POS[0]
                    cell_y = POS[1]
                    if self.tictactoe.markers[cell_x // 100][cell_y // 100] == 0:
                        self.tictactoe.markers[cell_x // 100][cell_y // 100] = self.tictactoe.player
                        self.tictactoe.player *= -1
                        self.tictactoe.check_winner()
        if self.tictactoe.game_over:
            self.tictactoe.draw_winner()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.check_events()


if __name__ == "__main__":
    app = App()
    app.run()
