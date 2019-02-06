def power(num, n):
	if n == 1: #terminating conndition
		return num
	else:
		return num * power(num, n-1) # calling itself and moving towards closing condition

power(2,3)