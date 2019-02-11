import os, itertools
clear = lambda: os.system('cls')

def win(current_game):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	# Horizontal
	for row in current_game:
		if all_same(row):
			print(f"Player {row[0]} won horizontally (-)")
			return True

	# Vertical
	for col in range(len(game)):
		check = []
		for row in game:
			check.append(row[col])
		if all_same(check):
			print(f"Player {row[0]} won vertically (|)")
			return True

	# Diagonal
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"Player {diags[0]} won diagonally (/)")
		return True
	diags = []
	for position in range(len(game)):
		diags.append(game[position][position])
	if all_same(diags):
		print(f"Player {diags[0]} won diagonally (\\)")
		return True

	return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
	# global game
	clear()
	try:
		if game_map[row][column] != 0:
			print(f"This position is occupied, choose another!")
			print(f"Current Player: {current_player}")
			return game_map, False
		print("   0  1  2")
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True
	except IndexError as e:
		print("Try insert row/column as 0, 1 or 2?", e)
		return game_map, False
	except Exception as e:
		print("Something went wrong", e)
		return game_map, False

play = True
while play:
	game = [
		[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]
	]
	game_won = False
	game, _ = game_board(game)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current Player: {current_player}")
		played = False

		while not played:
			column_choice = int(input("Which column? 0, 1, 2: "))
			row_choice = int(input("Which row? 0, 1, 2: "))
			game = game_board(game, current_player, row_choice, column_choice)
		
		if win(game):
			game_won = True
			again = input("Want another game? ('Y') to continue: ")
			if again.lower() == 'y':
				print("Restarting!")
			elif again.lower() == 'n':
				print("Bye!")
				play = False