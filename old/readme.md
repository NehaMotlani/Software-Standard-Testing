# Name - NEHA MOTLANI
# Email-id - neha.motlani@research.iiit.ac.in
# SSAD ASSIGNMENT 1 - BOMBERMAN

Mainly it cosists of files :
board.py
bricks.py
enemy.py
bomberman.py
bomb.py

# board.py contains the code to print the basic code.
 - Frist append the first two lines of board using loops.
 - From third line onwards ,you can observe that there are basically two patterns that need to be apppended.And using even-odd logic we can print that.
 Pattern 1 - [                              ......]
 			 [                              ......]
 Pattern 2 - [XXXX    XXXX    XXXX    XXXX    XXXX]
 			 [XXXX    XXXX    XXXX    XXXX    XXXX]
 - At last append the last two tines.
 -bprint() print the 2D array.

# In bricks.py 
- The board is imported .
- generate_b generates the bricks.
- Randomly some co-ordinates are generated and stored in an array.
- At these cordinates the matrix value is changed to '/'.(Logically co-ordinates contaning 'X' are skipped).
- A typical brick is = { //// }
					   { //// }
-

# In enemy.py
- bricks.py is imported.
- board is imported .
- bomb is imported.
- generate_e generates enemy.
- Randomly some co-ordinates are generated and stored in an array.
- At these cordinates the matrix value is changed to 'e'.(Logically co-ordinates contaning 'X' are skipped).
- moveEnemies is used for movement of enemy.
- For move, we randomly choose free direction and by free I mean there is no adjacent enemy or brick or wall is present.
- Enemy is denoted by = { eeee }
						{ eeee }

# In bomberman.py
- enemy is imported.
- bomb is imported.
- bricks is imported.
- generate_bomberman generates a bomberman.
- bomberman is represented by = { [^^] }
								{  ][  }
- moveBomberman handles its movements.
- Through keypress bomberman moves, if you press "a" it moves left , if you press "d" it moves right , if you press "s" it moves down and if you press "w" it moves up.
- If you press "b" it leaves a bomb at its position. 
- If it collides with enemy or if it is in range of bomb it loses a life.

# In bomb.py
- enemy is imported.
- bricks is imported.
- The board is inherited.
- explode is called when bombcounter turns 0. All the neighbouring blocks are turned to "e" accept for walls.
- All the blocks that turned into "e" are cleared i.e, replaced by " " using clearex.
- Bomb intially looks like = { [22] }
							 { [22] }
- The counter is decreamented using bombcounter (2 changes to 1 , 1 changes to 0,0 changes to e and the bomb explodes).

Total number of lives for each try is 3.

Bonus question of bob counter is implemented.

## Use python run.py to start the game. 


