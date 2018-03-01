'''Code for enemy'''
from random import randint
from board import Board
from bricks import bricks
import time
from bomb import *


class Enemy(Board, bricks):

    '''Enemy needs location of board and bricks'''

    Earraryx = []
    Earraryy = []

    # generates random co-ordinates and places enemy there
    # divide board into 15 X 12 blocks.
    # This process co-ordinates for these bloacks
    def __init__(self):
        pass

    def generate_e(self):
        '''Generates enemy'''

        i = 0
        while i < 6:
            west = randint(1, 15)
            uest = randint(1, 12)
            if west in self.Earraryx:
                continue
            if uest in self.Earraryy:
                continue
            self.Earraryx.append(west)
            self.Earraryy.append(uest)
            i = i + 1

        # print(self.arraryy)
        # print(self.arraryx)

        for j in range(0, 6):
            lest = self.Earraryx[j]
            qest = self.Earraryy[j]
            # if block cordinate are both even the a wall is present there and
            # at (1,1) bomberman is present
            if (lest % 2 == 0 and qest % 2 == 0) or (lest == 1 and qest == 1):
                continue
            else:
                # print(self.arraryx[j]),
                # print(self.arraryy[j])
                # print(Board.board)
                Board.board[lest * 2][qest * 4] = 'e'
                Board.board[2 * lest][4 * qest + 1] = 'e'
                Board.board[2 * lest][4 * qest + 2] = 'e'
                Board.board[2 * lest][4 * qest + 3] = 'e'
                Board.board[2 * lest + 1][4 * qest] = 'e'
                Board.board[2 * lest + 1][4 * qest + 1] = 'e'
                Board.board[2 * lest + 1][4 * qest + 2] = 'e'
                Board.board[2 * lest + 1][4 * qest + 3] = 'e'

    def moveEnemies(self):

        for j in range(0, 6):

            # This decides in which direction enemy will move
            # A random no. from 1 to 4 is generated and each of
            # these is associated to a direction.
            # It also checks if that direction is "free",
            temp = randint(1, 4)

            if temp == 1:
                stemp = 'up'
            elif temp == 2:
                stemp = 'down'
            elif temp == 3:
                stemp = 'right'
            elif temp == 4:
                stemp = 'left'
            # print("I")
            # print(self.Earraryx[j],self.Earraryy[j])
            ex = self.Earraryx[j] * 2
            ey = self.Earraryy[j] * 4
            # print(stemp)
            if stemp == 'up':
                # print("ut")
                if Board.board[ex - 2][ey + 1] == "^":
                    Bomb.lives -= 1
                    if Bomb.lives == 0:
                        quit()
                    # quit()
                if Board.board[ex - 2][ey] == 'e' or \
                    Board.board[ex - 2][ey] == 'X' \
                        or Board.board[ex - 2][ey] == '/':
                    continue
                    # stemp = 'down'
                else:
                    Board.board[ex - 2][ey] = 'e'
                    Board.board[ex - 2][ey + 1] = 'e'
                    Board.board[ex - 2][ey + 2] = 'e'
                    Board.board[ex - 2][ey + 3] = 'e'
                    Board.board[ex - 1][ey] = 'e'
                    Board.board[ex - 1][ey + 1] = 'e'
                    Board.board[ex - 1][ey + 2] = 'e'
                    Board.board[ex - 1][ey + 3] = 'e'
                    for u in range(0, 4):
                        Board.board[ex][ey + u] = ' '
                        Board.board[ex + 1][ey + u] = ' '
                    ex = ex - 2
                    ey = ey
                    self.Earraryx[j] = ex / 2
                    self.Earraryy[j] = ey / 4
                    # time.sleep(0.5)
                    # print("L")
                    # print(self.Earraryx[j],self.Earraryy[j])

            if stemp == 'down':
                # print("dt")
                if Board.board[ex + 2][ey + 1] == "^":
                    Bomb.lives -= 1
                    if Bomb.lives == 0:
                        quit()
                    # quit()
                if Board.board[ex + 2][ey] == 'e' or \
                    Board.board[ex + 2][ey] == 'X' \
                        or Board.board[ex + 2][ey] == '/':
                    continue
                    # stemp = 'right'
                else:
                    Board.board[ex + 2][ey] = 'e'
                    Board.board[ex + 2][ey + 1] = 'e'
                    Board.board[ex + 2][ey + 2] = 'e'
                    Board.board[ex + 2][ey + 3] = 'e'
                    Board.board[ex + 3][ey] = 'e'
                    Board.board[ex + 3][ey + 1] = 'e'
                    Board.board[ex + 3][ey + 2] = 'e'
                    Board.board[ex + 3][ey + 3] = 'e'
                    for u in range(0, 4):
                        Board.board[ex][ey + u] = ' '
                        Board.board[ex + 1][ey + u] = ' '
                    # time.sleep(0.5)

                    ex = ex + 2
                    ey = ey
                    self.Earraryx[j] = ex / 2
                    self.Earraryy[j] = ey / 4
                    # print("L")

                    # print(self.Earraryx[j],self.Earraryy[j])

            if stemp == 'right':
                # print("rt")
                if Board.board[ex][ey + 5] == "^":
                    Bomb.lives -= 1
                    if Bomb.lives == 0:
                        quit()
                    # quit()
                if Board.board[ex][ey + 4] == 'e' \
                    or Board.board[ex][ey + 4] == 'X' \
                        or Board.board[ex][ey + 4] == '/':
                    continue
                    # stemp = 'left'
                else:
                    Board.board[ex][ey + 4] = 'e'
                    Board.board[ex][ey + 5] = 'e'
                    Board.board[ex][ey + 6] = 'e'
                    Board.board[ex][ey + 7] = 'e'
                    Board.board[ex + 1][ey + 4] = 'e'
                    Board.board[ex + 1][ey + 5] = 'e'
                    Board.board[ex + 1][ey + 6] = 'e'
                    Board.board[ex + 1][ey + 7] = 'e'
                    for u in range(0, 4):
                        Board.board[ex][ey + u] = ' '
                        Board.board[ex + 1][ey + u] = ' '
                    # time.sleep(0.5)
                    ex = ex
                    ey = ey + 4
                    self.Earraryx[j] = ex / 2
                    self.Earraryy[j] = ey / 4
                    # print("L")
                    # print(self.Earraryx[j],self.Earraryy[j])

            if stemp == 'left':
                # print("lt")
                if Board.board[ex][ey - 3] == "^":
                    Bomb.lives -= 1
                    if Bomb.lives == 0:
                        quit()
                    # quit()
                if Board.board[ex][ey - 4] == 'e' \
                    or Board.board[ex][ey - 4] == 'X' \
                        or Board.board[ex][ey - 4] == '/':
                    continue
                else:
                    Board.board[ex][ey - 1] = 'e'
                    Board.board[ex][ey - 2] = 'e'
                    Board.board[ex][ey - 3] = 'e'
                    Board.board[ex][ey - 4] = 'e'
                    Board.board[ex + 1][ey - 1] = 'e'
                    Board.board[ex + 1][ey - 2] = 'e'
                    Board.board[ex + 1][ey - 3] = 'e'
                    Board.board[ex + 1][ey - 4] = 'e'
                    for u in range(0, 4):
                        Board.board[ex][ey + u] = ' '
                        Board.board[ex + 1][ey + u] = ' '
                    # time.sleep(0.5)
                    ex = ex
                    ey = ey - 4
                    self.Earraryx[j] = ex / 2
                    self.Earraryy[j] = ey / 4
                    # print("L")
                    # print(self.Earraryx[j],self.Earraryy[j])
