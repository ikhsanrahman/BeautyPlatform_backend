from app.api.create_app import db 
from app.api.db_model import *
from app.api.product.serializer import ProductSchema
from app.api.error import error
from flask import jsonify
from werkzeug.utils import secure_filename
import os

from app.api.config.config import Config

TIME = Config.time()
err = error.ProductError
FILE_FOLDER = Config.FILE_FOLDER

RANDOM_FILE_EXTENSIONS = set(['mp4', 'jpeg', 'jpg', 'png', 'mpeg', '3gp', 'webm', 'avi', 'mov'])

def allowed_file(filename):
	allowed = '.' in filename and filename.rsplit('.', 1)[1].lower() in RANDOM_FILE_EXTENSIONS
	if allowed is True:
		return True
	else :
		return err.badRequest("extension file is not allowed.")


class ProductProcess:

	def getProducts(self):
		products = FileSeller.query.filter_by(status_file=True).all()
		result = ProductSchema(many=True).dump(products).data
		if products :
			return jsonify(result)

		if not products:
			return err.requestFailed("no products available")

	def uploadProduct(self, payload, seller_id, item_id):
		seller = Seller.query.filter_by(id=seller_id).first()
		item = Item.query.filter_by(id=item_id).first()

		if not seller and not item:
			return err.requestFailed('you dont have access')

		file = payload['file_name']
		

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(FILE_FOLDER, filename))


		file_ = FileSeller.query.filter_by(file_title=payload['file_title']).first()

		if not file_ :
			new_file = FileSeller(file_title=payload['file_title'], file_name=filename, item=item.id )

			db.session.add(new_file)
			db.session.commit()
			return err.requestSuccess("upload file has succeed")

		if file_ :
			return err.badRequest("file with that title already existed")
		

	def updateProduct(self, payload, seller_id, item_id, product_id):
		seller = Seller.query.filter_by(id=seller_id).first()
		item = Item.query.filter_by(id=item_id).first()
		product = FileSeller.query.filter_by(id=product_id).first()

		if not seller and not item and not product:
			return err.requestFailed('you dont have access')

		file = payload['file_name']
		
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(FILE_FOLDER, filename))


		file_ = FileSeller.query.filter_by(file_title=payload['file_title']).first()

		if seller and item and product :
			product.file_title = payload['file_title']
			product.file_name = filename
			product.updated_at = TIME
			db.session.commit()
			return err.requestSuccess("update file product has succeed")

	def removeProduct(self, seller_id, item_id, product_id):
		seller = Seller.query.filter_by(id=seller_id).first()
		item = Item.query.filter_by(id=item_id).first()
		product = FileSeller.query.filter_by(id=product_id).first()

		if seller and item and product :
			for x in os.listdir(os.chdir("/home/ikhsan/github/beauty/beauty/data/file")):
				if product.file_name == x :
					os.remove(x)

			db.session.delete(product)
			db.session.commit()
			return err.requestSuccess("remove product has succeed")

		if not seller and not item and not product:
			return err.requestFailed("no product available")


	def unactivateProduct(self, product_id):
		product = FileSeller.query.filter_by(id=product_id).first()
		if seller :
			seller.status_file = False
			db.session.commit()
			return err.requestSuccess("unactivate product success")
		if not user :
			return err.requestFailed("no products can be unactivated")

	def reactivateSeller(self, product_id):
		product = FileSeller.query.filter_by(id=product_id).first()
		if product :
			if product.status_file == True:
				return err.requestFailed("product already active")
			if product.status_file == False:
				product.status_file = True
				db.session.commit()
				return err.requestSuccess("reactivate product has succeed")
		if not product:
			return err.badRequest("product is not available")

	def searchProductByName(self, payload):
		sellers = Seller.query.all()
		result = []
		for seller in sellers :
			if payload['full_name'] in seller.full_name :
				seller = SellerSchema().dump(seller).data
				result.append(seller)
		if result:
			return result

		return err.badRequest("No seller detected")
