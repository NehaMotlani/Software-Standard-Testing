from random import randint
from enemy import *
import signal,copy,sys,time
from getChar import _GetchUnix as getchar
from alarmexception import *
from board import *
from bricks import *
from bomb import Bomb

class bomberman(Board,bricks,Enemy,Bomb):

	x = 2
	y = 5
	# score = 0
	# This func. generates a bomberman at starting point.
	def generate_bomberman(self):
		Board.board[2][4]="["
		Board.board[2][5]="^"
		Board.board[2][6]="^"
		Board.board[2][7]="]"
		Board.board[3][4]=" "
		Board.board[3][5]="]"
		Board.board[3][6]="["
		Board.board[3][7]=" "
	# Takes a keypress and accordinly moves the bomberman.
	# a --> left
	# d --> right
	# s --> down
	# w --> up 
	def moveBomberman (self):
		def alarmHandler(signum, frame):
			raise AlarmException
		def user_input(timeout=0.1):
			signal.signal(signal.SIGALRM, alarmHandler)
			signal.setitimer(signal.ITIMER_REAL,timeout)
			try:
				text = getchar()()
				signal.alarm(0)
				return text
			except AlarmException:
				print("")
			signal.signal(signal.SIGALRM, signal.SIG_IGN)
			return ''

		key = user_input()
		previous = key
		# usermove = user_input()
		if(key=='q'):
			exit()
		#move left and emeny is not there
		if(key=='a' and Board.board[self.x][self.y-5]!="X" and Board.board[self.x][self.y-5]!="/" and Board.board[self.x][self.y-5]!="e"):
			# for u in range(0,4):
			# 	Board.board[self.x][self.y-2-u] = "b"
			# 	Board.board[self.x+1][self.y-2-u] = "b"
				Board.board[self.x][self.y-5] = "["
				Board.board[self.x][self.y-4] = "^"
				Board.board[self.x][self.y-3] = "^"
				Board.board[self.x][self.y-2] = "]"
				Board.board[self.x+1][self.y-5] = " "
				Board.board[self.x+1][self.y-4] = "]"
				Board.board[self.x+1][self.y-3] = "["
				Board.board[self.x+1][self.y-2] = " "
				for u in range(0,4):
					if(Board.board[self.x][self.y]=="2"):
						break
			 		Board.board[self.x][self.y-1+u] = ' '
			 		Board.board[self.x+1][self.y-1+u] = ' '
			 	self.x = self.x
			 	self.y = self.y - 4
		#move left and enemy is there
		if(key == "a" and Board.board[self.x][self.y-5]== "e"):
			Bomb.lives -= 1
			if(Bomb.lives==0):
				quit()
			# quit()
		#move right and enemy is not there
		if(key == "d" and Board.board[self.x][self.y+3]!= "X" and Board.board[self.x][self.y+3]!= "/" and Board.board[self.x+1][self.y+3]!= "e"):				
			Board.board[self.x][self.y+6] = "]"
			Board.board[self.x][self.y+5] = "^"
			Board.board[self.x][self.y+4] = "^"
			Board.board[self.x][self.y+3] = "["
			Board.board[self.x+1][self.y+3] = " "
			Board.board[self.x+1][self.y+5] = "["
			Board.board[self.x+1][self.y+4] = "]"
			Board.board[self.x+1][self.y+6] = " "
			for u in range(0,4):
				if(Board.board[self.x][self.y]=="2"):
					break
				Board.board[self.x][self.y-1+u] = ' '
				Board.board[self.x+1][self.y-1+u] = ' '
			self.x = self.x
			self.y = self.y + 4
		#move down and enemy is present
		if(key == "d" and Board.board[self.x][self.y+3]=="e"):
			Bomb.lives -= 1
			if(Bomb.lives==0):
				quit()
			# quit()
		#move up and emeny is not there
		if(key == "w" and Board.board[self.x-2][self.y]!="X" and Board.board[self.x-2][self.y]!="/" and Board.board[self.x-2][self.y]!="e"):
			Board.board[self.x-2][self.y-1] = "["
			Board.board[self.x-2][self.y] = "^"
			Board.board[self.x-2][self.y+1] = "^"
			Board.board[self.x-2][self.y+2] = "]"
			Board.board[self.x-1][self.y-1] = " "
			Board.board[self.x-1][self.y] = "]"
			Board.board[self.x-1][self.y+1] = "["
			Board.board[self.x-1][self.y+2] = " "
			for u in range(0,4):
				if(Board.board[self.x][self.y]=="2"):
					break
				Board.board[self.x][self.y-1+u] = ' '
				Board.board[self.x+1][self.y-1+u] = ' '
			self.x = self.x - 2
			self.y = self.y 

		#move up and enemy is there
		if(key == "w" and Board.board[self.x-2][self.y]=="e"):
			Bomb.lives -= 1
			if(Bomb.lives==0):
				quit()
			# quit()
		#move down and enemy is not there
		if(key == "s" and Board.board[self.x+2][self.y]!="X" and Board.board[self.x+2][self.y]!="/" and Board.board[self.x+2][self.y]!="e"):
			Board.board[self.x+2][self.y-1] = "["
			Board.board[self.x+2][self.y] = "^"
			Board.board[self.x+2][self.y+1] = "^"
			Board.board[self.x+2][self.y+2] = "]"
			Board.board[self.x+3][self.y-1] = " "
			Board.board[self.x+3][self.y] = "]"
			Board.board[self.x+3][self.y+1] = "["
			Board.board[self.x+3][self.y+2] = " "
			for u in range(0,4):
				if(Board.board[self.x][self.y]=="2"):
					break
				Board.board[self.x][self.y-1+u] = ' '
				Board.board[self.x+1][self.y-1+u] = ' '
			self.x = self.x+2
			self.y = self.y
		#move down and enemy is there
		if(key == "s" and Board.board[self.x+2][self.y]=="e"):
			Bomb.lives -= 1
			if(Bomb.lives==0):
				quit()
			# quit()
		if(key == "b"):
			# Board.board[self.x][self.y-1]="["
			# Board.board[self.x][self.y]="2"
			# Board.board[self.x][self.y+1]="2"
			# Board.board[self.x][self.y+2]="]"
			# Board.board[self.x+1][self.y-1]="["
			# Board.board[self.x+1][self.y]="2"
			# Board.board[self.x+1][self.y+1]="2"
			# Board.board[self.x+1][self.y+2]="]"
			
		 	Board.board[self.x][self.y-1]="["
			Board.board[self.x][self.y]="2"
			Board.board[self.x][self.y+1]="2"
			Board.board[self.x][self.y+2]="]"
			Board.board[self.x+1][self.y-1]="["
			Board.board[self.x+1][self.y]="2"
			Board.board[self.x+1][self.y+1]="2"
			Board.board[self.x+1][self.y+2]="]"
			Bomb.bombx.append(self.x)
			Bomb.bomby.append(self.y-1)


			# bo = Bomb()
			# bo.create_bomb(self.x,self.y-1)
			# Bomb.bombx.append(self.x)
			# Bomb.bomby.append(self.y-1)
			# for i in range(0,len(Bomb.bombx)):
			# 	print(Bomb.bombx[i])
			# 	print(Bomb.bomby[i])
			# bo.bombcount()
		# 	if(previous=="a"):
		# 		if(Board.board[self.x][self.y+3]!= "X" and Board.board[self.x][self.y+3]!= "/" and Board.board[self.x+1][self.y+3]!= "e"):				
		# 			Board.board[self.x][self.y+6] = "]"
		# 			Board.board[self.x][self.y+5] = "^"
		# 			Board.board[self.x][self.y+4] = "^"
		# 			Board.board[self.x][self.y+3] = "["
		# 			Board.board[self.x+1][self.y+3] = " "
		# 			Board.board[self.x+1][self.y+5] = "["
		# 			Board.board[self.x+1][self.y+4] = "]"
		# 			Board.board[self.x+1][self.y+6] = " "
		# 			for u in range(0,4):
		# 				Board.board[self.x][self.y-1+u] = '2'
		# 				Board.board[self.x+1][self.y-1+u] = '2'
		# 			self.x = self.x
		# 			self.y = self.y + 4
			 	 
		# 		if(Board.board[self.x][self.y+3]=="e"):
		# 			quit()
				
		# 	if(previous == "d"):
		# 		if(Board.board[self.x][self.y-5]!="X" and Board.board[self.x][self.y-5]!="/" and Board.board[self.x][self.y-5]!="e"):
		# 			Board.board[self.x][self.y-5] = "["
		# 			Board.board[self.x][self.y-4] = "^"
		# 			Board.board[self.x][self.y-3] = "^"
		# 			Board.board[self.x][self.y-2] = "]"
		# 			Board.board[self.x+1][self.y-5] = " "
		# 			Board.board[self.x+1][self.y-4] = "]"
		# 			Board.board[self.x+1][self.y-3] = "["
		# 			Board.board[self.x+1][self.y-2] = " "
		# 			for u in range(0,4):
		# 	 			Board.board[self.x][self.y-1+u] = '2'
		# 	 			Board.board[self.x+1][self.y-1+u] = '2'
		# 		 	self.x = self.x
		# 		 	self.y = self.y - 4
		# 			#move left and enemy is there
		# 			if(Board.board[self.x][self.y-5]== "e"):
		# 				quit()
		# 	if(previous == "w"):
		# 		if(Board.board[self.x+2][self.y]!="X" and Board.board[self.x+2][self.y]!="/" and Board.board[self.x+2][self.y]!="e"):
		# 			Board.board[self.x+2][self.y-1] = "["
		# 			Board.board[self.x+2][self.y] = "^"
		# 			Board.board[self.x+2][self.y+1] = "^"
		# 			Board.board[self.x+2][self.y+2] = "]"
		# 			Board.board[self.x+3][self.y-1] = " "
		# 			Board.board[self.x+3][self.y] = "]"
		# 			Board.board[self.x+3][self.y+1] = "["
		# 			Board.board[self.x+3][self.y+2] = " "
		# 			for u in range(0,4):
		# 				Board.board[self.x][self.y-1+u] = '2'
		# 				Board.board[self.x+1][self.y-1+u] = '2'
		# 			self.x = self.x+2
		# 			self.y = self.y
		# 		#move down and enemy is there
		# 		if(Board.board[self.x+2][self.y]=="e"):
		# 			quit()
		# 	if(previous == "s"):
		# 		if(Board.board[self.x-2][self.y]!="X" and Board.board[self.x-2][self.y]!="/" and Board.board[self.x-2][self.y]!="e"):
		# 			Board.board[self.x-2][self.y-1] = "["
		# 			Board.board[self.x-2][self.y] = "^"
		# 			Board.board[self.x-2][self.y+1] = "^"
		# 			Board.board[self.x-2][self.y+2] = "]"
		# 			Board.board[self.x-1][self.y-1] = " "
		# 			Board.board[self.x-1][self.y] = "]"
		# 			Board.board[self.x-1][self.y+1] = "["
		# 			Board.board[self.x-1][self.y+2] = " "
		# 			for u in range(0,4):
		# 				Board.board[self.x][self.y-1+u] = '2'
		# 				Board.board[self.x+1][self.y-1+u] = '2'
		# 			self.x = self.x - 2
		# 			self.y = self.y 

		# #move up and enemy is there
		# 		if(Board.board[self.x-2][self.y]=="e"):
		# 			quit()
				
		
		
