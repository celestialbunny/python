def some_decorator(my_func): # this is a decorator function
	def wrap_func():
		print("Execute this first before my function")

		my_func()

		print("Execute this after my function")

	return wrap_func # decorator functions always return a function without calling it e.g. `wrap_func()`

@some_decorator # adds functionality to `my_function`
def my_function():
	print("Hello World")

my_function()