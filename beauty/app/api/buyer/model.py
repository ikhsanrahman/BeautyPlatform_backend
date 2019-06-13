from app.api.create_app import db 
from app.api.db_model import *
from app.api.buyer.serializer import BuyerSchema
from app.api.error import error
from flask import jsonify

from app.api.config.config import Config

TIME = Config.time()
err = error.BuyerError

class BuyerProcess:

	def getBuyers(self):
		buyers = Buyer.query.filter_by(status_buyer=True).all()
		result = BuyerSchema(many=True).dump(buyers).data
		if buyers :
			return jsonify(result)

		if not buyers:
			return err.requestFailed("no seller available")

	def createBuyer(self, payload):
		responses = {}
		buyer = Buyer.query.filter_by(email=payload['email']).first()
		
		if not buyer:
			new_buyer = Buyer(full_name = payload['full_name'], email=payload['email'], \
								password=payload['password'], gender=payload['gender'], \
								phone_number=payload['phone_number'], address=payload['address'] )
			new_buyer.generate_password_hash(payload['password'])
			db.session.add(new_buyer)
			db.session.commit()
			return err.requestSuccess("register success")
		
		if buyer :
			return err.requestFailed("Buyer with that email already existed")

	def updateBuyer(self, payload, buyer_id):
		buyer = Buyer.query.filter_by(id=buyer_id).first()

		if buyer :
			buyer.full_name = payload['full_name']
			buyer.phone_number = payload ['phone_number']
			buyer.gender	= payload['gender']
			buyer.address	= payload['address']
			buyer.updated_at = TIME
			db.session.commit()
			return err.requestSuccess("update profil success")

		if not buyer:
			return err.badRequest("not available buyer")

	def removeBuyer(self, buyer_id):
		buyer = Buyer.query.filter_by(id=buyer_id).first()

		if buyer :
			db.session.delete(buyer)
			db.session.commit()
			return err.requestSuccess("remove buyer has succeed")
		if not buyer:
			return err.requestFailed("no buyer available")

	def updatePassword(self, payload, buyer_id):
		buyer = Buyer.query.filter_by(id=buyer_id, email=payload['email']).first()

		if buyer:
			buyer.password = payload['new_password']
			buyer.generate_password_hash(payload['new_password'])
			buyer.updated_at = TIME
			db.session.commit()
			return err.requestSuccess("edit password success")

		if not buyer:
			return err.requestFailed("buyer is not available")


	def forgetPassword(self, payload):
		buyer = Buyer.query.filter_by(email=payload['email']).first()

		if buyer:
			buyer.password = payload['new_password']
			buyer.generate_password_hash(payload['new_password'])
			buyer.updated_at = TIME
			db.session.commit()
			return err.requestSuccess("edit forget password success")

		if not buyer:
			return err.requestFailed("buyer is not available")

	def loginBuyer(self, payload):
		buyer = Buyer.query.filter_by(email=payload['email']).first()

		if buyer and buyer.check_password_hash(payload['password']):
			return err.requestSuccess("login success")
		return err.requestFailed("login failed")

	def unactivateBuyer(self, buyer_id):
		buyer = Buyer.query.filter_by(id=buyer_id).first()
		if buyer :
			buyer.status_buyer = False
			db.session.commit()
			return err.requestSuccess("unactivate buyer success")
		if not buyer :
			return err.requestFailed("no buyer can be unactivated")

	def reactivateBuyer(self, buyer_id):
		buyer = Buyer.query.filter_by(id=buyer_id).first()
		if buyer :
			if buyer.status_buyer == True:
				return err.requestFailed("buyer already active")
			if buyer.status_buyer == False:
				buyer.status_buyer = True
				db.session.commit()
				return err.requestSuccess("reactivate buyer has succeed")
		if not buyer:
			return err.badRequest("seller is not available")

	def searchBuyerByName(self, payload):
		buyers = Buyer.query.all()
		result = []
		for buyer in buyers :
			if payload['full_name'] in buyer.full_name :
				buyer_ = BuyerSchema().dump(buyer).data
				result.append(buyer_)
		if result:
			return result

		return err.badRequest("No buyer detected")
