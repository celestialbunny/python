import random, string
import sys
sys.stdout.flush()
# first_row = []
# second_row = []
# third_row = []

# def create_row(row_appended):
# 	for x in range(0, 4):
# 		row_appended.append(random.choice(string.ascii_uppercase))

# create_row(first_row)
# create_row(second_row)
# create_row(third_row)
# print(first_row)
# print(second_row)
# print(third_row)

'''
uncomment the row and column limit to decide on the display
'''
# row_count = 4
# column_count = 4
row_count = 16
column_count = 6

i = 0
while(i < row_count):
	j = 0
	while(j < column_count):
		captured_output = random.choice(string.ascii_uppercase)
		if captured_output == 'Q':
			captured_output = 'Qu'
		print(f"{captured_output}   ", end="", flush=True)
		j = j + 1
	print("\t")
	i = i + 1

	# Array.split(", ") will turn
	# 'Ken, Alena, Jessie' => into
	# ['Ken', 'Alena', 'Jessie']