from random import randint
from board import *

class bricks(Board):

	arraryx = []
	arraryy = []

	def generate_b(self):
		for i in range(0,10):
			self.arraryx.append(randint(1,15))#17
			self.arraryy.append(randint(1,12))#14

		# print(self.arraryy)
		# print(self.arraryx)

		for j in range(0,10):
			a = self.arraryx[j]
			b = self.arraryy[j]
				
			if((a%2==0 and b%2==0) or (a==1 and b==1)):
				continue
			else:
				# print(self.arraryx[j]),
				# print(self.arraryy[j]) 
				# print(Board.board)
				Board.board[ a*2 ][ b*4 ] = '/'
				Board.board[2*a][4*b+1] = '/'
				Board.board[2*a][4*b+2] = '/'
				Board.board[2*a][4*b+3] = '/'
				Board.board[2*a+1][4*b] = '/'
				Board.board[2*a+1][4*b+1] = '/'
				Board.board[2*a+1][4*b+2] = '/'
				Board.board[2*a+1][4*b+3] = '/'
