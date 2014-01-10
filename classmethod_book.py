class Book:
	def __init__(self, price):
		self.price = price

	def get_price_by(self, tax):
		return self.price * tax

	def get_price(self):
		