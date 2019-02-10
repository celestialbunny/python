import os
from itertools import cycle

clear = lambda: os.system('cls')
# player_turn = cycle(range(2))

game = [
	[0, 1, 1],
	[0, 1, 0],
	[0, 1, 0]
]

no_winner = True

def game_board(player_turn, row, column):
	clear()
	print("   0  1  2")
	# print(type(player_turn))
	game[row][column] = player_turn
	for count, row in enumerate(game):
		print(count, row)

def check_horizontal(no_winner):
	if game[0][0] == game[0][1] and game[0][1] == game[0][2]:
		no_winner = False
	if game[1][0] == game[1][1] and game[1][1] == game[0][2]:
		no_winner = False
	if game[2][0] == game[2][1] and game[2][1] == game[0][2]:
		no_winner = False
	return no_winner

def check_vertical(no_winner):
	if game[0][0] == game[1][0] and game[1][0] == game[2][0]:
		no_winner = False
	if game[0][1] == game[1][1] and game[1][1] == game[2][1]:
		no_winner = False
	if game[0][2] == game[1][2] and game[1][2] == game[2][2]:
		no_winner = False
	return no_winner

def check_diagonal(no_winner):
	if game[0][0] == game[1][1] and game[1][1] == game[2][2]:
		no_winner = False
	elif game[0][2] == game[1][1] and game[1][1] == game[2][0]:
		no_winner = False
	return no_winner

def find_winner(no_winner):
	if check_horizontal(no_winner) or check_vertical(no_winner) or check_diagonal(no_winner):
		no_winner = False
	return no_winner

# game_board(1, 0, 0)

# while no_winner:
# 	input1, input2, input3 = input().split()
# 	player_turn = int(input1)
# 	row = int(input2)
# 	column = int(input3)
# 	if game[row][column] == 0:
# 		game_board(player_turn, row, column)
# 	else:
# 		print("Space occupied")
# 	find_winner()
# 	if not no_winner:
# 		print(f"Player {player_turn} won")

print(check_horizontal(no_winner))
print(check_vertical(no_winner))
print(check_diagonal(no_winner))
print(find_winner(no_winner))