from bomberman import *
import time
import os
from bomb import *

# import subprocess
# import sys
	 
# for scriptInstance in [1,2,3]:
# 	sys.stdout=open('result%s.txt' % scriptInstance,'w')
# 	subprocess.check_call(['python','run.py'], \
# 		stdout=sys.stdout, stderr=subprocess.STDOUT)






# lives = 3
# while(lives>0):
b = bomberman()
b.generate_board()
	#########b.bprint()
b.generate_bomberman()
	#########b.bprint()
b.generate_b()
	#########b.bprint()
b.generate_e()
b.bprint()
i=0
	# print(start)
while True:
		# print("time")
		# print(int(time.time()))
		# print(start)
		# if(int(time.time())==start+1):
		# 	b.moveEnemies()
		# 	b.bprint()
		# 	print(start)
		# start = start + 1
		# # i = i + 1
		# # if (i>1000):
		# # 	break
		# start = int(time.time())
			
		# os.system("clear")
	b.bprint()
	print("")
	print("YOUR SCORE ="),
	print(b.score),
	print(" ")
	print("NUMBER OF LIVES LEFT ="),
	print(b.lives-1)
	# print(start)
	if(i%15==0):
		b.moveEnemies()	
		b.bombcount()
	b.moveBomberman()
	i = i + 1
	# timer(3,b.moveEnemies())




