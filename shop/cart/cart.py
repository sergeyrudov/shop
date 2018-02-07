MY_CART = 'mycart'

class Cart:
	def __init__(self, session):
		self.session = session
		if session.get(MY_CART):
			self.cart = session[MY_CART].copy()
		else:
			self.cart = []
			
	def product_index(self, id):
		for i in range(0, len(self.cart)):
			if self.cart[i][0] == id:
				return i
				
	def add_product(self, id, quantity):
		index = self.product_index(id)
		if index is None:
			self.cart.append([id, quantity])
		else:
			self.cart[index][1] += quantity
		self.save()
			
	def save(self):
		self.session[MY_CART] = self.cart
		
		
	def remove_product(self, id, quantity):
		index = self.product_index(id)
		
	def show_cart(self):
		return self.cart
		
	def price_counter(self):
		