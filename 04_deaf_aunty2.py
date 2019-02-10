import string

magic_word = "I love you aunty, I have to go now"
user_input = ''

soft_input = "WHAT? SPEAK UP!"
loud_input = "YOU ARE VERY RUDE!"
mix_input = "SHOW SOME RESPECT!"

# 'Password must contain a lowercase letter'
def has_lowercase(user_input):
	return len(set(string.ascii_lowercase).intersection(user_input)) > 0

# 'Password must contain an uppercase letter'
def has_uppercase(user_input):
	return len(set(string.ascii_uppercase).intersection(user_input)) > 0

username = input("What is your name: ")
while user_input != magic_word:
	user_input = input("Say something: \n")
	# branching whether user input CONTAINS lower OR upper
	if has_lowercase(user_input):
		# branching whether user input CONTAINS mixed OR lower
		if has_uppercase(user_input):
			if user_input != magic_word:
				print(mix_input)
			else:
				print("ok. Goodbye")
				exit_input_1 = input(f'{username}, are you there?')
				if (exit_input_1 == ''):
					exit_input_2 = input('{username}, are you there?')
					if (exit_input_2 == ''):
						break
					else:
						user_input = ''
				else:
					user_input = ''
		else:
			print(soft_input)
	elif has_uppercase(user_input):
		print(loud_input)