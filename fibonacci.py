store = [0, 1]
def fibonacci(number):
	for loop in range(0, number-2):
		count = store[-1] + store[-2]
		store.append(count)

fibonacci(8)
print(store)