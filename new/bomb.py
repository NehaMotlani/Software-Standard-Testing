'''Code for Bomb'''
from enemy import *
from bricks import bricks
from board import Board
# from bomberman import *
# from run import *


class Bomb(Board):
    bombx = []
    bombyest = []
    score = 0
    lives = 3

    def __init__(self):
        pass
    # def create_bomb(self,a,b):
    # 	Board.board[a][b]="["
    # 	Board.board[a][b+1]="2"
    # 	Board.board[a][b+2]="2"
    # 	Board.board[a][b+3]="]"
    # 	Board.board[a+1][b]="["
    # 	Board.board[a+1][b+1]="2"
    # 	Board.board[a+1][b+2]="2"
    # 	Board.board[a+1][b+3]="]"
    # 	self.bombx.append(a)
    # 	self.bombyest.append(b)

    # All neighbouring blocks near the bomb are exploded. And if you break a
    # wall or kill an enemy using bomb u get 20 and 100 resp.
    def explode(self, xest, yest):
        baest = xest
        byest = yest
        for uest in range(0, 4):
            Board.board[baest][byest + uest] = 'e'
            Board.board[baest + 1][byest + uest] = 'e'

        byest = byest + 4
        if Board.board[baest][byest] == "e":
            self.score = self.score + 100
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'

        if Board.board[baest][byest + 1] == "^":
            quit()

        if Board.board[baest][byest] == "/":
            self.score = self.score + 20
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'

        if Board.board[baest][byest + 1] == "2" or \
            Board.board[baest][byest + 1] == "1"or \
                Board.board[baest][byest + 1] == "0":
            explode(baest, byest)
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'
        if Board.board[baest][byest] == "X":
            pass
        if Board.board[baest][byest] == " ":
            # bomberman.b.score = bomberman.b.score + 20
            for u in range(0, 4):
                Board.board[baest][byest + u] = 'e'
                Board.board[baest + 1][byest + u] = 'e'
        byest = byest - 4

        byest = byest - 4
        if Board.board[baest][byest] == "e":
            self.score = self.score + 100
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'

        if Board.board[baest][byest + 1] == "^":
            quit()

        if Board.board[baest][byest] == "/":
            self.score = self.score + 20
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'

        if Board.board[baest][byest + 1] == "2" or \
            Board.board[baest][byest + 1] == "1"or \
                Board.board[baest][byest + 1] == "0":
            explode(baest, byest)
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'
        if Board.board[baest][byest] == "X":
            pass
        if Board.board[baest][byest] == " ":
            # bomberman.b.score = bomberman.b.score + 20
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'
        byest = byest + 4

        baest = baest + 2
        if Board.board[baest][byest] == "e":
            self.score = self.score + 100
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'

        if Board.board[baest][byest + 1] == "^":
            quit()

        if Board.board[baest][byest] == "/":
            self.score = self.score + 20
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'

        if Board.board[baest][byest + 1] == "2" or \
            Board.board[baest][byest + 1] == "1"\
                or Board.board[baest][byest + 1] == "0":
            explode(baest, byest)
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'
        if Board.board[baest][byest] == "X":
            pass
        if Board.board[baest][byest] == " ":
            # bomberman.b.score = bomberman.b.score + 20
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'
        baest = baest - 2

        baest = baest - 2
        if Board.board[baest][byest] == "e":
            self.score = self.score + 100
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'

        if Board.board[baest][byest + 1] == "^":
            quit()

        if Board.board[baest][byest] == "/":
            self.score = self.score + 20
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'

        if Board.board[baest][byest + 1] == "2" or \
            Board.board[baest][byest + 1] == "1"or \
                Board.board[baest][byest + 1] == "0":
            explode(baest, byest)
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'
        if Board.board[baest][byest] == "X":
            pass
        if Board.board[baest][byest] == " ":
            # bomberman.b.score = bomberman.b.score + 20
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = 'e'
                Board.board[baest + 1][byest + uest] = 'e'
        baest = baest + 2

    def clearex(self, a, b):
        baest = a
        byest = b

        for uest in range(0, 4):
            Board.board[baest][byest + uest] = ' '
            Board.board[baest + 1][byest + uest] = ' '
        byest = byest + 4
        if Board.board[baest][byest] == "e":
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = ' '
                Board.board[baest + 1][byest + uest] = ' '
        byest = byest - 4

        byest = byest - 4
        if Board.board[baest][byest] == "e":
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = ' '
                Board.board[baest + 1][byest + uest] = ' '
        byest = byest + 4

        baest = baest + 2
        if Board.board[baest][byest] == "e":
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = ' '
                Board.board[baest + 1][byest + uest] = ' '
        baest = baest - 2

        baest = baest - 2
        if Board.board[baest][byest] == "e":
            for uest in range(0, 4):
                Board.board[baest][byest + uest] = ' '
                Board.board[baest + 1][byest + uest] = ' '
        baest = baest + 2
    # @staticmethod

    def bombcount(self):
        # for i in range(0,len(Bomb.bombx)):
            # print(Bomb.bombx[i])
            # print(Bomb.bombyest[i])

        for uest in range(0, len(Bomb.bombx)):
            boa = Bomb.bombx[uest]
            bob = Bomb.bombyest[uest]
            # print(a)
            # print(b)
            if Board.board[boa][bob + 1] == "2":
                Board.board[boa][bob] = "["
                Board.board[boa][bob + 1] = "1"
                Board.board[boa][bob + 2] = "1"
                Board.board[boa][bob + 3] = "]"
                Board.board[boa + 1][bob] = "["
                Board.board[boa + 1][bob + 1] = "1"
                Board.board[boa + 1][bob + 2] = "1"
                Board.board[boa + 1][bob + 3] = "]"

            elif Board.board[boa][bob + 1] == "1":
                Board.board[boa][bob] = "["
                Board.board[boa][bob + 1] = "0"
                Board.board[boa][bob + 2] = "0"
                Board.board[boa][bob + 3] = "]"
                Board.board[boa + 1][bob] = "["
                Board.board[boa + 1][bob + 1] = "0"
                Board.board[boa + 1][bob + 2] = "0"
                Board.board[boa + 1][bob + 3] = "]"

            elif Board.board[boa][bob + 1] == "0":
                Board.board[boa][bob] = "e"
                Board.board[boa][bob + 1] = "e"
                Board.board[boa][bob + 2] = "e"
                Board.board[boa][bob + 3] = "e"
                Board.board[boa + 1][bob] = "e"
                Board.board[boa + 1][bob + 1] = "e"
                Board.board[boa + 1][bob + 2] = "e"
                Board.board[boa + 1][bob + 3] = "e"
                Bomb.explode(self, boa, bob)

            elif Board.board[boa][bob] == "e":
                Bomb.clearex(self, boa, bob)
