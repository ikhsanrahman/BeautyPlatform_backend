from flask_restplus import Namespace, fields

class Home:
	api = Namespace('Home', description='api related to first access')

class Buyer :
	api = Namespace('Buyer', description='api related to Buyer')

class Seller :
	api = Namespace('Seller', description='api related to Seller ')

class Item:
	api = Namespace('Item', description='api related to Item')

class Admin:
	api = Namespace('admin', description="api for monitoring apps")

class Product:
	api = Namespace('Product', description="api for product")
