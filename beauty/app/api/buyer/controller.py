import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.buyer.serializer import *
from app.api.buyer.model import BuyerProcess
from app.api.request_schema import *
from app.api.config import config
from app.api.error import error
from app.api.namespace import Buyer, Home

api = Buyer.api
home = Home.api
err = error.SellerError

@home.route('')
class Home(Resource):
    def get(self) :
        responses = {}
        responses['Entry Gate'] = "Welcome to Beauty Platform E-Commerce " 
        return jsonify(Opening=responses)
    
@api.route('/login')
class BuyerLogin(Resource) :
    def get(self):
        payload = LoginBuyerRequestSchema().parser.parse_args(strict=True)
        if payload['password'] != payload['confirm_password']:
            return err.badRequest("password doesnt not match")
            
        errors = LoginBuyerSchema().load(payload).errors
        if errors:
            return errors

        result = BuyerProcess().loginBuyer(payload)
        return result

@api.route('/search')
class SearchNameBuyer(Resource) :

    @api.doc('search buyer by name')
    def get(self) :
        payload = SearchBuyerNameRequestSchema().parser.parse_args(strict=True)

        searchBuyer = BuyerProcess().searchBuyerByName(payload)
        return searchBuyer


@api.route('')
class Seller(Resource):
    @api.doc('get all Buyer')
    def get(self):

        result = BuyerProcess().getBuyers() 
        return result
    #end def

    @api.doc('registering new buyer')
    def post(self):
        
        payload = RegisterBuyerRequestSchema().parser.parse_args(strict=True)

        errors = BuyerSchema().load(payload).errors
        if errors :
            return errors

        result = BuyerProcess().createBuyer(payload)
        return result

    def put(self):
        payload = ForgetPasswordRequestSchema().parser.parse_args(strict=True)
        errors = ForgetPasswordSchema().load(payload).errors
        if errors:
            return errors

        result = BuyerProcess().forgetPassword(payload)
        return result

@api.route('/<int:buyer_id>')
class UpdateDeleteSeller(Resource):
    
    @api.doc('update a buyer')
    def put(self, buyer_id):
       
        payload = UpdateBuyerRequestSchema().parser.parse_args(strict=True)
        print(payload)
        errors = UpdateBuyerSchema().load(payload).errors
        if errors :
            return errors

        updateBuyer = BuyerProcess().updateBuyer(payload, buyer_id)
        return updateBuyer
    #end def

    @api.doc('remove a buyer')
    def delete(self, buyer_id):
        result = BuyerProcess().buyerSeller(buyer_id)
        return result


@api.route('/<int:buyer_id>/updatepassword')
class UpdatePasswordBuyer(Resource):
    
    @api.doc('update password buyer')
    def put(self, buyer_id):
       
        payload = UpdatePasswordRequestSchema().parser.parse_args(strict=True)

        if payload['new_password'] != payload['confirm_new_password'] :
            return err.requestFailed("password doesnt match")

        errors = UpdatePasswordSchema().load(payload).errors
    
        if errors :
            return errors

        updatePassword = BuyerProcess().updatePassword(payload, buyer_id)
        return updatePassword
    #end def



@api.route('/<int:buyer_id>/unactivate')
class UnactivateBuyer(Resource):
    #@auth.login_required
    @api.doc('delete a buyer')
    def get(self, buyer_id) :

        result = BuyerProcess().unactivateBuyer(buyer_id)
        return result
    #end def
#end class

@api.route('/<int:buyer_id>/reactivate')
class ReactivateBuyer(Resource) :
      
    def get(self, buyer_id) :
        result = BuyerProcess().reactivateBuyer(buyer_id)
        return result
    #end def
#end class

@api.route('/destroyTableSeller')
class destroyDatabase(Resource):

    # @auth.login_required
    def delete(self):
        tableOff = BuyerProcess().tableOff()
        return tableOff







