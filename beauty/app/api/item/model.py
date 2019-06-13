from app.api.create_app import db 
from app.api.db_model import *
from app.api.item.serializer import ItemSchema
from app.api.error import error
from flask import jsonify

from app.api.config.config import Config

TIME = Config.time()
err = error.ItemError

class ItemProcess:

	def getItems(self, seller_id):
		sellers = Seller.query.filter_by(id=seller_id).first()
		items = Item.query.all()
		result = ItemSchema(many=True).dump(items).data
		if sellers :
			if result :
				return jsonify(result)
			return err.badRequest("no item")
		if not sellers:
			return err.requestFailed("no seller available")

	def createItem(self, payload, seller_id):
		responses = {}
		seller = Seller.query.filter_by(id=seller_id).first()
		item = Item.query.filter_by(item_title=payload['item_title']).first()

		if seller:
			if not item:
				new_item = Item(item_title = payload['item_title'], description=payload['description'], \
									price=payload['price'] )
				db.session.add(new_item)
				db.session.commit()
				return err.requestSuccess("create item success")
			return err.badRequest("item with that title already existed") 
		if not seller :
			return err.requestFailed("you dont have access to this page")

	def updateItem(self, payload, seller_id, item_id):
		seller = Seller.query.filter_by(id=seller_id).first()
		item = Item.query.filter_by(id=item_id).first()

		if seller :
			if item:
				item.item_title = payload['item_title']
				item.description = payload ['description']
				item.price	= payload['price']
				item.updated_at = TIME
				db.session.commit()
				return err.requestSuccess("update item success")
			return err.badRequest("no such that item")
		if not seller:
			return err.badRequest("not available seller")

	def removeSeller(self, seller_id, item_id):
		responses = {}
		seller = Seller.query.filter_by(id=seller_id).first()
		item = Item.query.filter_by(id=item_id).first()

		if seller :
			if item:
				db.session.delete(seller)
				db.session.commit()
				return err.requestSuccess("remove seller has succeed")
			return err.badRequest("no such that item")
		if not seller:
			return err.requestFailed("no seller available")
