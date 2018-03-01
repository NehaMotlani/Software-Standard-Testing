'''Code for Board'''
from random import randint
# import getCh
# from getCh import _GetchUnix as getChar
# import threading
# from threading import Thread
# import signal,copy,sys,time
# from * import alarmexception
# from alarmexception import *
# import curses
# from sys import exit


class Board:

    def __init__(self):
        pass

    board = [[] for i in range(34)]
    # board = [[]]

    def generate_board(self):
        '''Generatesthe board'''
        lest = []
        u = 0
        i = 0
        for i in range(0, 2):
            for j in range(0, 84):
                lest.append("X")
            self.board[u] = lest
            # board[u].append(l)
            u = u + 1
            lest = []
            #   print(u)

                # l.append("")
            # print(l)
        i = 0
        for i in range(0, 15):
            if i % 2 == 0:
                for k in range(0, 2):
                    for j in range(0, 84):
                        if j > 3 and j < 80:
                            lest.append(" ")
                        else:
                            lest.append("X")
                    self.board[u] = lest
                    # board[u].append(l)
                    u = u + 1
                    lest = []
            #           print(u)
                        # l.append("")
            else:
                for k in range(0, 2):
                    for z in range(0, 21):
                        if z % 2 == 0:
                            for x in range(0, 4):
                                lest.append("X")
                        else:
                            for x in range(0, 4):
                                lest.append(" ")
                    self.board[u] = lest
                    # board[u].append(l)
                    u = u + 1
                    lest = []
            #           print(u)

                        # l.append("")
        for i in range(0, 2):
            for j in range(0, 84):
                lest.append("X")
            self.board[u] = lest
            # board[u].append(l)
            u = u + 1
            lest = []
        # print(u)
    # print(board)
        # print("")

    def bprint(self):
        for i in range(0, 34):
            for j in range(0, 84):
                print self.board[i][j],
            print ""




# bo = Board()
# brick = bricks()
# brick.generateb()
# e = Enemy()
# e.generatee()
# b = bomberman()
# b.moveright()
# bo.bprint()
