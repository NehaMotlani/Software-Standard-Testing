from enemy import *
from bricks import *
from board import *
# from bomberman import *
# from run import *

class Bomb(Board):
	bombx = []
	bomby = []
	score = 0
	lives = 3
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
	# 	self.bomby.append(b)


	# All neighbouring blocks near the bomb are exploded. And if you break a wall or kill an enemy using bomb u get 20 and 100 resp. 
	def explode(self,x,y):
		ba = x
		by = y
		for u in range(0,4):
			Board.board[ba][by+u] = 'e'
			Board.board[ba+1][by+u] = 'e'

		by = by + 4
		if(Board.board[ba][by]=="e"):
			self.score = self.score + 100
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'

		if(Board.board[ba][by+1]=="^"):
			quit()

		if(Board.board[ba][by]=="/"):
			self.score = self.score + 20
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'

		if(Board.board[ba][by+1]=="2" or Board.board[ba][by+1]=="1"or Board.board[ba][by+1]=="0"):
				explode(ba,by)
				for u in range(0,4):
					Board.board[ba][by+u] = 'e'
					Board.board[ba+1][by+u] = 'e'
		if(Board.board[ba][by]=="X"):
			pass
		if(Board.board[ba][by]==" "):
			# bomberman.b.score = bomberman.b.score + 20
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		by = by - 4

		by = by - 4
		if(Board.board[ba][by]=="e"):
			self.score = self.score + 100
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'

		if(Board.board[ba][by+1]=="^"):
			quit()

		if(Board.board[ba][by]=="/"):
			self.score = self.score + 20
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'

		if(Board.board[ba][by+1]=="2" or Board.board[ba][by+1]=="1"or Board.board[ba][by+1]=="0"):
			explode(ba,by)
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		if(Board.board[ba][by]=="X"):
			pass
		if(Board.board[ba][by]==" "):
			# bomberman.b.score = bomberman.b.score + 20
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		by = by + 4

		ba = ba + 2
		if(Board.board[ba][by]=="e"):
			self.score = self.score + 100
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		
		if(Board.board[ba][by+1]=="^"):
			quit()
		
		if(Board.board[ba][by]=="/"):
			self.score = self.score + 20
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		
		if(Board.board[ba][by+1]=="2" or Board.board[ba][by+1]=="1"or Board.board[ba][by+1]=="0"):
			explode(ba,by)
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		if(Board.board[ba][by]=="X"):
			pass
		if(Board.board[ba][by]==" "):
			# bomberman.b.score = bomberman.b.score + 20
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		ba = ba - 2

		ba = ba - 2
		if(Board.board[ba][by]=="e"):
			self.score = self.score + 100
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		
		if(Board.board[ba][by+1]=="^"):
			quit()
		
		if(Board.board[ba][by]=="/"):
			self.score = self.score + 20
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		
		if(Board.board[ba][by+1]=="2" or Board.board[ba][by+1]=="1"or Board.board[ba][by+1]=="0"):
			explode(ba,by)
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		if(Board.board[ba][by]=="X"):
			pass
		if(Board.board[ba][by]==" "):
			# bomberman.b.score = bomberman.b.score + 20
			for u in range(0,4):
				Board.board[ba][by+u] = 'e'
				Board.board[ba+1][by+u] = 'e'
		ba = ba + 2

	def clearex(self,a,b):
		ba = a
		by = b

		for u in range(0,4):
				Board.board[ba][by+u] = ' '
				Board.board[ba+1][by+u] = ' '
		by = by + 4
		if(Board.board[ba][by]=="e"):
			for u in range(0,4):
				Board.board[ba][by+u] = ' '
				Board.board[ba+1][by+u] = ' '
		by = by - 4

		by = by - 4
		if(Board.board[ba][by]=="e"):
			for u in range(0,4):
				Board.board[ba][by+u] = ' '
				Board.board[ba+1][by+u] = ' '
		by = by + 4

		ba = ba + 2
		if(Board.board[ba][by]=="e"):
			for u in range(0,4):
				Board.board[ba][by+u] = ' '
				Board.board[ba+1][by+u] = ' '
		ba = ba - 2

		ba = ba - 2
		if(Board.board[ba][by]=="e"):
			for u in range(0,4):
				Board.board[ba][by+u] = ' '
				Board.board[ba+1][by+u] = ' '
		ba = ba + 2
	# @staticmethod
	def bombcount(self):
		# for i in range(0,len(Bomb.bombx)):
			# print(Bomb.bombx[i])
			# print(Bomb.bomby[i])

		for u in range(0,len(Bomb.bombx)):
			boa = Bomb.bombx[u]
			bob = Bomb.bomby[u]
			# print(a)
			# print(b)
			if(Board.board[boa][bob+1]=="2"):
				Board.board[boa][bob]="["
				Board.board[boa][bob+1]="1"
				Board.board[boa][bob+2]="1"
				Board.board[boa][bob+3]="]"
				Board.board[boa+1][bob]="["
				Board.board[boa+1][bob+1]="1"
				Board.board[boa+1][bob+2]="1"
				Board.board[boa+1][bob+3]="]"

			elif(Board.board[boa][bob+1]=="1"):
				Board.board[boa][bob]="["
				Board.board[boa][bob+1]="0"
				Board.board[boa][bob+2]="0"
				Board.board[boa][bob+3]="]"
				Board.board[boa+1][bob]="["
				Board.board[boa+1][bob+1]="0"
				Board.board[boa+1][bob+2]="0"
				Board.board[boa+1][bob+3]="]"

			elif(Board.board[boa][bob+1]=="0"):
				Board.board[boa][bob]="e"
				Board.board[boa][bob+1]="e"
				Board.board[boa][bob+2]="e"
				Board.board[boa][bob+3]="e"
				Board.board[boa+1][bob]="e"
				Board.board[boa+1][bob+1]="e"
				Board.board[boa+1][bob+2]="e"
				Board.board[boa+1][bob+3]="e"
				Bomb.explode(self,boa,bob)

			elif(Board.board[boa][bob]=="e"):
				Bomb.clearex(self,boa,bob)








	
