from random import randint
# import getCh
# from getCh import _GetchUnix as getChar
# import threading
# from threading import Thread
# import signal,copy,sys,time
# # from * import alarmexception
# # from alarmexception import *
# import curses
# from sys import exit


class Board:


	board = [[] for i in range(34)]
	# board = [[]]
	def generate_board(self):
		l = []
		u=0
		i = 0 
		for i in range(0,2):
			for j in range(0,84):
				l.append("X")
			self.board[u] = l
			#board[u].append(l)
			u = u+1
			l = []
			#	print(u)

				#l.append("")
			#print(l)
		i = 0
		for i in range(0,15):
			if(i%2==0):
				for k in range(0,2):
					for j in range(0,84):
						if(j>3 and j<80):
							l.append(" ")
						else:
							l.append("X")
					self.board[u] = l
					#board[u].append(l)
					u = u+1
					l = []
			#			print(u)
						#l.append("")
			else:
				for k in range(0,2):
					for z in range(0,21):
						if(z%2==0):
							for x in range(0,4):
								l.append("X")
						else:
							for x in range(0,4):
								l.append(" ")
					self.board[u] = l
					#board[u].append(l)	
					u=u+1
					l = []
			#			print(u)

						#l.append("")
		for i in range(0,2):
			for j in range(0,84):
				l.append("X")
			self.board[u] = l
			#board[u].append(l)
			u=u+1
			l = []
		#print(u)
	#print(board)
		#print("")	
	
	
	def bprint(self):
		for i in range(0,34):
			for j in range(0,84):
				print(self.board[i][j]),
			print("")




# bo = Board()
# brick = bricks()
# brick.generateb()
# e = Enemy()
# e.generatee()
# b = bomberman()
# # b.moveright()
# bo.bprint()