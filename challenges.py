# importing for Error 3
from countryinfo import CountryInfo

# Error 1
def mean(*numbers):
	print(type(numbers))
	total = sum(numbers)
	return print(total / len(numbers))
mean(5, 3, 6, 10)

# Error 2
def user_details(name, occupation):
	return print(f"Hi! My name is {name} and I am a {occupation}.")
user_details("Glo", "Lecturer")

# Error 3
def apple_price(num_of_apples):
	country = CountryInfo('Malaysia')
	amount = num_of_apples * 1.15
	return print(f"The price for {num_of_apples} will be {country.currencies()} {amount}")
apple_price(15)

# Error 4
def run():
	return "This is the method 'run' and it did not take in any arguments!"
print(run())

# Error 5
initial_adult_population = 1600.0
def adult_male_population(n):
	return n * 0.4
def adult_female_population(n):
	return n * 0.6
def total_babies(n):
	return adult_male_population(n * 10)
def total_female(n):
	female_adult = adult_female_population(n)
	female_babies = total_babies(n) * 0.6
	total = female_adult + female_babies
	return total
print(total_female(initial_adult_population))

# Challenge: Factorials
def factorials(num):
	if num == 1:
		return num
	else:
		return num * factorials(num-1)

print(factorials(5))

# Challenge: Fibonacci
store = [0, 1]
def fibonacci(number):
	for loop in range(0, number-2):
		count = store[-1] + store[-2]
		store.append(count)

fibonacci(8)
print(store)