import string

# 'Password must contain a lowercase letter'
def has_lowercase(user_input):
	return len(set(string.ascii_lowercase).intersection(user_input)) > 0

# 'Password must contain an uppercase letter'
def has_uppercase(user_input):
	return len(set(string.ascii_uppercase).intersection(user_input)) > 0

def determine_outcome(scenario):
	category = 0
	if has_lowercase(scenario):
		category = 1
	if has_uppercase(scenario):
		category = 2
	if has_lowercase(scenario) and has_uppercase(scenario):
		category = 3
	if scenario == MAGIC_WORD:
		category = 4
	return category

name = input("What is your name: ")
while True:
	MAGIC_WORD = "I love you aunty, I have to go now"
	SOFT_INPUT = "WHAT? SPEAK UP!"
	LOUD_INPUT = "YOU ARE VERY RUDE!"
	MIX_INPUT = "SHOW SOME RESPECT!"

	response = input("Speak up: \n")

	outcome = determine_outcome(response)
	if outcome == 4:
		print("OK, goodbye")
		captcha1 = input(f"{name}, are you there?")
		if captcha1 != '':
			continue
		captcha2 = input(f"{name}, are you there?")
		if captcha2 != '':
			continue
		break
	else:
		if outcome == 1:
			print(SOFT_INPUT)
		elif outcome == 2:
			print(LOUD_INPUT)
		elif outcome == 3:
			print(MIX_INPUT)
		else:
			continue