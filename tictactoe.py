from termcolor import colored
import numpy as np
import random
import time
import os

global boardValues
global Prob
Prob = np.array([[0.5]*3 for i in range(3)])
# global lProb
# lProb = np.array([[0.5]*3 for i in range(3)])

# Print Game Board
def printBoard():
	print(" |  C O L")
	print(" |--1-2-3-")
	print("R|" + "1" + "|" + str(boardValues[0][0]) + "|" + str(boardValues[0][1]) + "|" + str(boardValues[0][2]) + "|")
	print(" |--------")
	print("O|" + "2" + "|" + str(boardValues[1][0]) + "|" + str(boardValues[1][1]) + "|" + str(boardValues[1][2]) + "|")
	print(" |--------")
	print("W|" + "3" + "|" + str(boardValues[2][0]) + "|" + str(boardValues[2][1]) + "|" + str(boardValues[2][2]) + "|")
	print(" |--------")

# Print Winning Board
# def finalBoard(j):
# 	print(" |  C O L")
# 	print(" |--1-2-3-")
# 	print("R|" + "1" + "|" + str(boardValues[0][0]) + "|" + str(boardValues[0][1]) + "|" + str(boardValues[0][2]) + "|")
# 	print(" |--------")
# 	print("O|" + "2" + "|" + str(boardValues[1][0]) + "|" + str(boardValues[1][1]) + "|" + str(boardValues[1][2]) + "|")
# 	print(" |--------")
# 	print("W|" + "3" + "|" + str(boardValues[2][0]) + "|" + str(boardValues[2][1]) + "|" + str(boardValues[2][2]) + "|")
# 	print(" |--------")


# def printProb():
# 	print(" |  C O L")
# 	print(" |--1-2-3-")
# 	print("R|" + "1" + "|" + str(lProb[0][0]) + "|" + str(lProb[0][1]) + "|" + str(lProb[0][2]) + "|")
# 	print(" |--------")
# 	print("O|" + "2" + "|" + str(lProb[1][0]) + "|" + str(lProb[1][1]) + "|" + str(lProb[1][2]) + "|")
# 	print(" |--------")
# 	print("W|" + "3" + "|" + str(lProb[2][0]) + "|" + str(lProb[2][1]) + "|" + str(lProb[2][2]) + "|")
# 	print(" |--------")

# Check if any player has won
def winCheck(i, turn):
	for j in range(len(boardValues)):
		# if (set(boardValues[j]) == {turn}) or (set(boardValues[:, j]) == {turn}) or (set(boardValues.diagonal()) == {turn}) or (set(np.fliplr(boardValues).diagonal()) == {turn}):
			# return True
		if set(boardValues[j]) == {turn}:
			# finalBoard(j)
			return True
		elif set(boardValues[:, j]) == {turn}:
			# finalBoard(j)
			return True
		elif set(boardValues.diagonal()) == {turn}:
			# finalBoard()
			return True
		elif set(np.fliplr(boardValues).diagonal()) == {turn}:
			# finalBoard()
			return True
	return False

# Calculate Winning Probability
# def wProbability(turn):
# 	di = False
# 	if ((x-1) + (y-1))%2 == 0:
# 		di = True
# 	for i in range(3):
# 		if i == x-1:
# 			count_i = list(boardValues[i]).count(turn)
# 			# count_x_i = list(boardValues[i]).count("X")
# 		for j in range(3):
# 			wProb[i][j] -= (count_i)/3
# 			if j == y-1:
# 				count_j = list(boardValues[:, j]).count(turn)
# 				# count_x_j = list(boardValues[:, j]).count("X")
# 				wProb[i][j] -= (count_j)/3
# 			if di and (i + j)%2 == 0:
# 				wProb[i][j] = list(boardValues.diagonal()).count(turn)/3

# Calculate Probabilty
# def Probability(turn, x, y):
# 	cp = "X"
# 	if turn == "X":
# 		cp = "O"
# 	di = False
# 	if ((x-1) + (y-1))%2 == 0:
# 		di = True
# 	for i in range(3):
# 		if i == x-1:
# 			# count_p_i = list(boardValues[i]).count(turn)
# 			# count_c_i = list(boardValues[i]).count(cp)
# 			for j in range(3):
# 				Prob[i][j] += (list(boardValues[i]).count(turn) + list(boardValues[i]).count(cp))/3
# 				if j == y-1:
# 					# count_p_j = list(boardValues[:, j]).count(turn)
# 					# count_c_j = list(boardValues[:, j]).count(cp)
# 					Prob[i][j] -= (list(boardValues[:, j]).count(turn) + list(boardValues[:, j]).count(cp))/3
# 				if di and (i + j)%2 == 0:
# 					Prob[i][j] = (list(boardValues.diagonal()).count(turn) + list(boardValues.diagonal()).count(cp))/3

# Player's input with Validation
def playerInput(i, turn):
	print("Player ",i+1," enter your place number as row,column")
	flag = True
	while(flag):
		try:
			xy = str(input())
			x = int(xy.split(",")[0])
			y = int(xy.split(",")[1])
		except Exception as e:
			print("Invalid Input\nEnter row,column")
		else:
			flag = False
			if x not in (1,2,3) or y not in (1,2,3):
				print("Invalid row or column\nEnter 1/2/3")
				flag = True

	exit = 0
	while (len(xy.split(",")) != 2) or ('' in xy.split(",")):
		print("Invalid Input\nPlease try Again")
		exit += 1
		flag = True
		while(flag):
			try:
				xy = str(input())
				x = int(xy.split(",")[0])
				y = int(xy.split(",")[1])
			except Exception as e:
				print("Invalid Input\nEnter row,column")
			else:
				flag = False
				if x not in (1,2,3) or y not in (1,2,3):
					print("Invalid row or column\nEnter 1/2/3")
					flag = True

	# Probability
	# Probability(turn, x, y)
	
	if boardValues[x-1][y-1] != " ":
		print("Place Already Taken")
		playerInput(i, turn)

	else:
		boardValues[x-1][y-1] = turn

# Computer's input with Validation
def computerInput(turn):
	print("Computer Input")

	# Probability(turn)
	# li = []
	# for prob in Prob:
	# 	li.extend(prob)
	# m_prob = max(li)
	
	# if li.count(m_prob) > 1:
	# 	pass

	
	x = random.randint(1,3)
	y = random.randint(1,3)
	while boardValues[x-1][y-1] != " ":
		x = random.randint(1,3)
		y = random.randint(1,3)

	print(x,y,turn)
	boardValues[x-1][y-1] = turn

# Player vs Player
def playerPlayer():
	print("Player 1 is X")
	print("Player 2 is O")

	i = 0
	moves = 0
	turn = ""
	while(True and moves < 9):
		i = i%2
		if i+1 == 1:
			turn = "X"

		elif i+1 == 2:
			turn = "O"

		playerInput(i, turn)
		os.system('clear')
		printBoard()
		if winCheck(i+1, turn):
			print("Player ",i+1," wins")
			break

		i += 1
		moves += 1

	if moves == 9:
		print("Match Draw")

# Player vs Computer
def playerComputer():
	print("Would you like to be X/x or O/o?")
	flag = True
	while(flag):
		try:
			preferance = str(input())
		except Exception as e:
			print("Invalid Input\nEnter X/x or O/o")
		else:
			flag = False
			if preferance not in ("X","x","O","o"):
				print("Invalid Input\nEnter X/x or O/o")
				flag = True
	
	if preferance == "X" or preferance == "x":
		turn = "O"
		preferance = "X"
		i = 0

	elif preferance == "O" or preferance == "o":
		turn = "X"
		preferance = "O"
		i = 1

	print("Player is",preferance)
	print("Computer is",turn)

	moves = 0
	while(True and moves < 9):
		i = i%2
		if i+1 == 1:
			playerInput(i, preferance)

		elif i+1 == 2:
			computerInput(turn)
			# time.sleep(5)
		os.system('clear')
		printBoard()
		# printProb()

		if i+1 == 1 and winCheck(i+1, preferance):
			print("Player ",i+1," wins")
			break

		elif i+1 == 2 and winCheck(i+1,turn):
			print("Computer wins")
			break

		i += 1
		moves += 1
	
	if moves == 9:
		print("Match Draw")

# Main Function
if __name__ == "__main__":
	game = "y"
	while(game == "y"):
		os.system('clear')
		boardValues = np.array([[" "]*3 for i in range(3)])
		print("TIC TAC TOE")
		print("1. Player vs Player\n2. Player vs Computer")
		
		flag = True
		while(flag):
			try:
				options = int(input())
			except Exception as e:
				print("Invalid Input\nEnter 1 or 2")
			else:
				flag = False
				if options not in (1,2):
					print("Invalid Input\nEnter 1 or 2")
					flag = True
		
		printBoard()
		if options == 1:
			playerPlayer()

		elif options == 2:
			playerComputer()

		print("Start Another Game?[y/n]")
		flag = True
		while(flag):
			try:
				game = str(input())
			except Exception as e:
				print("Invalid Input\nEnter y/n")
			else:
				flag = False
				# print(game)
				if game not in ("y", "n"):
					print("Invalid Input\nEnter y/n")
					flag = True


