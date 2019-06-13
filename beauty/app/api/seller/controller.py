import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.seller.serializer import *
from app.api.seller.model import SellerProcess
from app.api.request_schema import *
from app.api.config import config
from app.api.error import error
from app.api.namespace import Seller, Home

api = Seller.api
home = Home.api
err = error.SellerError

@home.route('')
class Home(Resource):
    def get(self) :
        responses = {}
        responses['Entry Gate'] = "Welcome to Beauty Platform E-Commerce " 
        return jsonify(Opening=responses)
    
@api.route('/login')
class SellerLogin(Resource) :
    def get(self):
        payload = LoginSellerRequestSchema().parser.parse_args(strict=True)
        if payload['password'] != payload['confirm_password']:
            return err.badRequest("password doesnt not match")
            
        errors = LoginSellerSchema().load(payload).errors
        if errors:
            return errors

        result = SellerProcess().loginSeller(payload)
        return result

@api.route('/search')
class SearchNameSeller(Resource) :

    @api.doc('search seller by name')
    def get(self) :
        payload = SearchSellerNameRequestSchema().parser.parse_args(strict=True)

        searchSeller = SellerProcess().searchSellerByName(payload)
        return searchSeller


@api.route('')
class Seller(Resource):
    @api.doc('get all seller')
    def get(self):

        result = SellerProcess().getSellers() 
        return result
    #end def

    @api.doc('registering new seller')
    def post(self):
        
        payload = RegisterSellerRequestSchema().parser.parse_args(strict=True)

        # if payload['password'] != payload['confirm_password']:
        #     return err("the password not match")

        errors = SellerSchema().load(payload).errors
        if errors :
            return errors

        result = SellerProcess().createSeller(payload)
        return result

    def put(self):
        payload = ForgetPasswordRequestSchema().parser.parse_args(strict=True)
        errors = ForgetPasswordSchema().load(payload).errors
        if errors:
            return errors

        result = SellerProcess().forgetPassword(payload)
        return result

@api.route('/<int:seller_id>')
class UpdateDeleteSeller(Resource):
    
    @api.doc('update a Seller')
    def put(self, seller_id):
       
        payload = UpdateSellerRequestSchema().parser.parse_args(strict=True)

        errors = UpdateSellerSchema().load(payload).errors
        if errors :
            return errors

        updateSeller = SellerProcess().updateSeller(payload, seller_id)
        return updateSeller
    #end def

    @api.doc('remove a seller')
    def delete(self, seller_id):
        removeSeller = SellerProcess().removeSeller(seller_id)
        return removeSeller


@api.route('/<int:seller_id>/updatePassword')
class UpdatePasswordSeller(Resource):
    
    @api.doc('update password seller')
    def put(self, seller_id):
       
        payload = UpdatePasswordRequestSchema().parser.parse_args(strict=True)

        if payload['new_password'] != payload['confirm_new_password'] :
            return err.requestFailed("password doesnt match")

        errors = UpdatePasswordSchema().load(payload).errors
    
        if errors :
            return errors

        updatePassword = SellerProcess().updatePassword(payload, seller_id)
        return updatePassword
    #end def



@api.route('/<int:seller_id>/unactivate')
class UnactivateSeller(Resource):
    #@auth.login_required
    @api.doc('delete a seller')
    def get(self, seller_id) :

        unactivateSeller = SellerProcess().unactivateSeller(seller_id)
        return unactivateSeller
    #end def
#end class

@api.route('/<int:seller_id>/reactivate')
class ReactivateSeller(Resource) :
      
    def get(self, seller_id) :
        reactivateSeller = SellerProcess().reactivateSeller(seller_id)
        return reactivateSeller
    #end def
#end class

@api.route('/destroyTableSeller')
class destroyDatabase(Resource):

    # @auth.login_required
    def delete(self):
        tableOff = SellerProcess().tableOff()
        return tableOff







