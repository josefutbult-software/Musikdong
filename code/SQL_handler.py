import default_config
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='musikdong',
                             unix_socket='/run/mysqld/mysqld.sock',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

class NotInDatabase(Exception):
   # Raised when an item doesn't exist in the database
   pass

class IncorrectProductDeclaration(Exception):
   # Raised when an attempt at creating a product object fails
   pass

class DuplicationError(Exception):
   # Raised when an attempt at inserting a duplicate object into the database
   pass


# Simple product class
class Product():
	def __init__(self, values):

		# Makes sure the declaration of the object is made by a working dictionary
		if values.get("id") is None or values.get("name") is None:
			raise IncorrectProductDeclaration

		self.id = values.get("id")
		self.name = values.get("name")	

# Returns a product item from the database as a dict
def getProductFromDatabase(id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM product WHERE id=%s", (id, ))
        try:
        	return Product((dict)(cursor.fetchone())) # Why does this work? This shouldn't be a feature!
        except:
        	raise NotInDatabase


def insertProductIntoDatabase(product: Product) -> None:
	if not isinstance(product, Product):
		raise TypeError

	with connection.cursor() as cursor:	
		try:
			cursor.execute("INSERT INTO `product` (`id`, `name`) VALUES (%s, %s)", (product.id, product.name))
			connection.commit()
		except:
			raise DuplicationError



# product = Product({'id': '000003', 'name': 'Ompa Drive'})
# insertProductIntoDatabase(product)
print(getProductFromDatabase('000003').name)
