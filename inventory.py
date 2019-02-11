class Product:
	def __init__(self, name, description, quantity, price):
		self.name = name
		self.description = description
		self.quantity = quantity
		self.price = price

	def __repr__(self):
		print(f"{self.name}: {self.description}, each of them costs {self.price}. There are {self.quantity} remaining.")
		print("\n")

	def item_delivery(self, amount):
		self.quantity = self.quantity - amount

class Warehouse:
	def __init__(self, name, location):
		self.name = name
		self.location = location
		self.products = []

	def __repr__(self):
		print(f"{self.name} at location {self.location} has: ")
		# print(f"{self.products}")
		for product in self.products:
			print(f"{product.name}")
		print("\n")

	def add_product(self, product):
		self.products.append(product)

class Store:
	def __init__(self, name, location):
		self.name = name
		self.location = location
		self.warehouses = []

snicker = Product(name="snicker", description="Chocolate energy bar", quantity=10000, price=1.2)
kitkat = Product(name="kitkat", description="Chocolate snack bar", quantity=2000, price=1)
kfc = Product(name="kfc", description="tastiest fried chicken", quantity=2000, price=1)
mcd = Product(name="mcd", description="simplest burger", quantity=2000, price=1)
h2o = Product(name="h2o", description="water, of course", quantity=2000, price=1)

wh_one = Warehouse(name="wh_one", location="Malaysia")
wh_two = Warehouse(name="wh_two", location="Singapore")
wh_three = Warehouse(name="wh_three", location="Thailand")

snicker.__repr__()
wh_one.add_product(snicker)
wh_one.add_product(kitkat)
wh_one.__repr__()
wh_two.add_product(kfc)
wh_two.add_product(mcd)
wh_two.__repr__()
wh_three.add_product(h2o)
wh_three.__repr__()

for item in wh_one.products:
	print(item.name)