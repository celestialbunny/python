# from countryinfo import CountryInfo
from datetime import datetime

# country = CountryInfo('Malaysia')
# country_currency = country.currencies()

class Money:
	def __init__(self, value, currency='MYR'):
		self.currency = currency
		self.value = value

	def __repr__(self):
		return (f"{self.currency}{self.value}")

class AccountHolder:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return (f"{self.name} is an account holder")

class Account:
	class_counter = 0
	def __init__(self, account_holder, balance=0, start_date=datetime.now().strftime('%A %B %d, %Y %I:%M%p')):
		self.account_number = Account.class_counter
		self.account_holder = account_holder
		self.balance = balance
		self.start_date = start_date
		Account.class_counter += 1

	def deposit(self, amount):
		# amount = input("What is the amount to be deposited: ")
		if amount > 0:
			self.balance += amount
		else:
			print("Please enter only valid numbers.")

	def withdrawal(self, amount):
		# amount = input("What is the amount to be withdrawn: ")
		if amount > 0 and amount <= self.balance:
			self.balance -= amount
		elif amount > self.balance:
			print("The requested amount is larger than your current savings.")
		else:
			print("Please enter only valid numbers.")

	def transfer(self, transferee, amount):
		if amount > 0 and amount <= self.balance:
			self.balance -= amount
			transferee.balance += amount
		elif amount > self.balance:
			print("The requested amount is larger than your current savings.")
		else:
			print("Please enter only valid numbers.")

	def __repr__(self):
		return (f"Account {self.account_number} is owned by {self.account_holder.name} having {self.balance} balance, created at {self.start_date}")



rm1 = Money(currency='MYR', value=1)
rm5 = Money(currency='MYR', value=5)
rm10 = Money(currency='MYR', value=10)
rm20 = Money(currency='MYR', value=20)
rm50 = Money(currency='MYR', value=50)
rm100 = Money(currency='MYR', value=100)
rm1.__repr__()
rm5.__repr__()
rm10.__repr__()
rm20.__repr__()
rm50.__repr__()
rm100.__repr__()

# now = datetime.now()
# current_time = now.strftime('%A %B %d, %Y %I:%M%p')
# print(current_time)

alex = AccountHolder(name="Alex")
cc = AccountHolder(name="CC")
alex_account0 = Account(alex)
alex_account1 = Account(alex)
cc_account0 = Account(cc)
alex_account0.__repr__()
print(cc_account0)
cc_account0.deposit(500)
print(cc_account0)
cc_account0.transfer(alex_account0,200)
print(cc_account0)
print(alex_account0)
