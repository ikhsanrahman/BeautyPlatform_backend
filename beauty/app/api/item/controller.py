import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.item.serializer import *
from app.api.item.model import ItemProcess
from app.api.request_schema import *
from app.api.config import config
from app.api.error import error
from app.api.namespace import Item

# RESPONSES_MSG = config.Config.RESPONSES_MSG
api = Item.api
err = error.ItemError


######################### ITEMS #############################

@api.route('/<int:seller_id>/item')
class Item(Resource):

    # @auth.login_required
    def get(self, seller_id):
        result = ItemProcess().getItems(seller_id)
        return result

    def post(self, seller_id):
        payload = UploadItemRequestSchema().parser.parse_args(strict=True)

        errors = ItemSchema().load(payload).errors
        if errors :
            return errors

        result = ItemProcess().createItem(payload, seller_id)
        return result

@api.route('/<int:seller_id>/<int:item_id>/editremove')
class EditDeleteItem(Resource):
    
    @api.doc('update a item')
    def put(self, seller_id, item_id):
       
        payload = UpdateItemRequestSchema().parser.parse_args(strict=True)

        errors = UpdateItemSchema().load(payload).errors
        if errors :
            return errors

        updateItem = ItemProcess().updateItem(payload, seller_id, item_id)
        return updateItem
    #end def

    @api.doc('remove a item')
    def delete(self, seller_id, item_id):
        removeItem = ItemProcess().removeItem(seller_id, item_id)
        return removeItem




