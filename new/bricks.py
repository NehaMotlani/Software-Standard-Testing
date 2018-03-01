'''Code for Bricks'''
from random import randint
from board import Board


class bricks(Board):

    '''Functionality of bricks'''
    arraryx = []
    arraryy = []

    def __init__(self):
        pass

    def generate_b(self):
        '''Generates Bricks'''
        for i in range(0, 10):
            self.arraryx.append(randint(1, 15))  # 17
            self.arraryy.append(randint(1, 12))  # 14
            i = i + 1
            i = i - 1
        # print(self.arraryy)
        # print(self.arraryx)

        for j in range(0, 10):
            aest = self.arraryx[j]
            best = self.arraryy[j]

            if (aest % 2 == 0 and best % 2 == 0) or (aest == 1 and best == 1):
                continue
            else:
                # print(self.arraryx[j]),
                # print(self.arraryy[j])
                # print(Board.board)
                Board.board[aest * 2][best * 4] = '/'
                Board.board[2 * aest][4 * best + 1] = '/'
                Board.board[2 * aest][4 * best + 2] = '/'
                Board.board[2 * aest][4 * best + 3] = '/'
                Board.board[2 * aest + 1][4 * best] = '/'
                Board.board[2 * aest + 1][4 * best + 1] = '/'
                Board.board[2 * aest + 1][4 * best + 2] = '/'
                Board.board[2 * aest + 1][4 * best + 3] = '/'
