class NotInDatabase(Exception):
   # Raised when an item doesn't exist in the database
   pass


class IncorrectObjectDeclaration(Exception):
   # Raised when an attempt at creating a product object fails
   pass


class DuplicationError(Exception):
   # Raised when an attempt at inserting a duplicate object into the database
   pass


# Simple product class
class Product():
	def __init__(self, values):

		# Makes sure the declaration of the object is made by a working dictionary
		if values.get("id") is None or values.get("name") is None or values.get("price") is None or values.get("description") is None or values.get("name") is None or values.get("category") is None:
			raise IncorrectObjectDeclaration

		self.id = values.get("id")
		self.name = values.get("name")
		self.price = values.get("price")
		self.description = values.get("description")
		self.imageUrl = values.get("imageUrl")
		self.category = values.get("category")


# A Simple tag class
class Tag():
	def __init__(self, values):

		# Makes sure the declaration of the object is made by a working dictionary
		if values.get("tagTypeName") is None or values.get("productId") is None:
			raise IncorrectObjectDeclaration

		self.tagTypeName = values.get("tagTypeName")
		self.productId = values.get("productId")
		

class User():
	def __init__(self, values):

		# Makes sure the declaration of the object is made by a working dictionary
		if values.get("id") is None or values.get("username") is None or values.get("password") is None or values.get("alias") is None:
			raise IncorrectObjectDeclaration

		self.id = values.get("id")
		self.username = values.get("username")
		self.password = values.get("password")
		self.alias = values.get("alias")
		
		