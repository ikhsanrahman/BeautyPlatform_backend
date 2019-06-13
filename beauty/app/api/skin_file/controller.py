import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.skin_file.serializer import *
from app.api.skin_file.model import ProductProcess
from app.api.request_schema import *
from app.api.config import config
from app.api.error import error
from app.api.namespace import SkinFile, Home

api = SkinFile.api
home = Home.api
err = error.ProductError


@api.route('/search')
class SearchNameSkinFile(Resource) :

    @api.doc('search skin file by name')
    def get(self) :
        payload = SearchSkinFileNameRequestSchema().parser.parse_args(strict=True)

        result = SkinFileProcess().searchSkinFileByName(payload)
        return result

@api.route('')
class GetProducts(Resource) :
    @api.doc('get all product')
    def get(self):
        result = ProductProcess().getProducts() 
        return result

@api.route('/<int:seller_id>/<int:item_id>/product')
class Product(Resource):
    @api.doc('upload new product')
    def post(self, seller_id, item_id):
        
        payload = UploadProductRequestSchema().parser.parse_args(strict=True)
        print(payload)
        errors = ProductSchema().load(payload).errors

        if errors :
            return errors

        result = ProductProcess().uploadProduct(payload, seller_id, item_id)
        return result

@api.route('/<int:seller_id>/<int:item_id>/<int:product_id>/updatedelete')
class UpdateDeleteSeller(Resource):
    
    @api.doc('update a product')
    def put(self, seller_id, item_id, product_id):
       
        payload = UpdateProductRequestSchema().parser.parse_args(strict=True)

        errors = UpdateProductSchema().load(payload).errors
        print(errors)
        if errors :
            return errors

        updateProduct = ProductProcess().updateProduct(payload, seller_id, item_id, product_id)
        return updateProduct
    #end def

    @api.doc('remove a product')
    def delete(self, seller_id, item_id, product_id):
        removeSeller = ProductProcess().removeProduct(seller_id, item_id, product_id)
        return removeSeller

