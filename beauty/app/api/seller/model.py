from app.api.create_app import db 
from app.api.db_model import *
from app.api.seller.serializer import SellerSchema
from app.api.error import error
from flask import jsonify

from app.api.config.config import Config

TIME = Config.time()
err = error.SellerError

class SellerProcess:

	def getSellers(self):
		sellers = Seller.query.filter_by(status_seller=True).all()
		result = SellerSchema(many=True).dump(sellers).data
		if sellers :
			return jsonify(result)

		if not sellers:
			return err.requestFailed("no seller available")

	def createSeller(self, payload):
		responses = {}
		seller = Seller.query.filter_by(email=payload['email']).first()
		
		if not seller:
			new_seller = Seller(full_name = payload['full_name'], email=payload['email'], \
								password=payload['password'], gender=payload['gender'], \
								phone_number=payload['phone_number'] )
			new_seller.generate_password_hash(payload['password'])
			db.session.add(new_seller)
			db.session.commit()
			return err.requestSuccess("register success")
		
		if user :
			return err.requestFailed("Seller with that email already existed")

	def updateSeller(self, payload, seller_id):
		seller = Seller.query.filter_by(id=seller_id).first()

		if seller :
			seller.full_name = payload['full_name']
			seller.phone_number = payload ['phone_number']
			seller.gender	= payload['gender']
			seller.updated_at = TIME
			db.session.commit()
			return err.requestSuccess("update profil success")

		if not seller:
			return err.badRequest("not available seller")

	def removeSeller(self, seller_id):
		responses = {}
		seller = Seller.query.filter_by(id=seller_id).first()

		if seller :
			db.session.delete(seller)
			db.session.commit()
			return err.requestSuccess("remove seller has succeed")
		if not seller:
			return err.requestFailed("no seller available")

	def updatePassword(self, payload, seller_id):
		seller = Seller.query.filter_by(id=seller_id, email=payload['email']).first()

		if seller:
			seller.password = payload['new_password']
			seller.generate_password_hash(payload['new_password'])
			seller.updated_at = TIME
			db.session.commit()
			return err.requestSuccess("edit password success")

		if not seller:
			return err.requestFailed("seller is not available")


	def forgetPassword(self, payload):
		seller = Seller.query.filter_by(email=payload['email']).first()

		if seller:
			seller.password = payload['new_password']
			seller.generate_password_hash(payload['new_password'])
			seller.updated_at = TIME
			db.session.commit()
			return err.requestSuccess("edit forget password success")

		if not seller:
			return err.requestFailed("seller is not available")

	def loginSeller(self, payload):
		seller = Seller.query.filter_by(email=payload['email']).first()

		if seller and seller.check_password_hash(payload['password']):
			return err.requestSuccess("login success")
		return err.requestFailed("login failed")

	def unactivateSeller(self, seller_id):
		seller = Seller.query.filter_by(id=seller_id).first()
		if seller :
			seller.status_seller = False
			db.session.commit()
			return err.requestSuccess("unactivate seller success")
		if not user :
			return err.requestFailed("no seller can be unactivated")

	def reactivateSeller(self, seller_id):
		seller = Seller.query.filter_by(id=seller_id).first()
		if seller :
			if seller.status_seller == True:
				return err.requestFailed("user already active")
			if seller.status_seller == False:
				seller.status_seller = True
				db.session.commit()
				return err.requestSuccess("reactivate seller has succeed")
		if not seller:
			return err.badRequest("seller is not available")

	def searchSellerByName(self, payload):
		sellers = Seller.query.all()
		result = []
		for seller in sellers :
			if payload['full_name'] in seller.full_name :
				seller = SellerSchema().dump(seller).data
				result.append(seller)
		if result:
			return result

		return err.badRequest("No seller detected")
