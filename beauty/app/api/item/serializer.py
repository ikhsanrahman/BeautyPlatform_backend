import re

from marshmallow import Schema, fields, ValidationError, post_load, validates
from app.api.create_app import db


def cannot_be_blank(string):
    if not string:
        raise ValidationError(" Data cannot be blank")
#end def

class ItemSchema(Schema):
    id                  = fields.Int()
    item_title          = fields.String(required=True, validate=cannot_be_blank)
    description         = fields.String(required=True, validate=cannot_be_blank)
    price               = fields.String(required=True, validate=cannot_be_blank)
    status_item         = fields.Method("bool_to_status")
    created_at          = fields.DateTime()
    updated_at          = fields.DateTime()
    deleted_at          = fields.DateTime()
    # video            = fields.String(load_only)
    # paper            = fields
        
    
    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status_item != True:
            status = "INACTIVE"
        return status
    #end def

    @validates('item_title')
    def validate_item_title(self, item_title):
        # allow all character
        pattern = r"^[a-z-A-Z_0-9 ]+$"
        if len(item_title) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(self.item_title))
        if len(item_title) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(self.item_title))
        if  re.match(pattern, item_title) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(self.item_title))
    #end def

    @validates('description')
    def validate_description(self, description):
        # allow all characters except number
        pattern = r"."
        if len(description) < 2:
            raise ValidationError('Invalid description, min is 2 characters')
        if len(description) > 1000:
            raise ValidationError('Invalid description, min is 1000 character')
        if re.match(pattern,description) is None:
            raise ValidationError(' see the rule of description')

    @validates('price')
    def validate_price(self, price):
        # allow all character
        pattern = r"^[0-9]+$"
        if len(price) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(self.price))
        if len(price) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(self.price))
        if  re.match(pattern, price) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(self.price))
    #end def

class UpdateItemSchema(Schema):

    id                  = fields.Int()
    item_title          = fields.String(required=True, validate=cannot_be_blank)
    price               = fields.String(required=True, validate=cannot_be_blank)
    description         = fields.String(required=True, validate=cannot_be_blank)
    status_item         = fields.Method("bool_to_status")
    created_at          = fields.DateTime()
    updated_at          = fields.DateTime()
    deleted_at          = fields.DateTime()
    # video            = fields.String(load_only)
    # paper            = fields
        
    
    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status_item != True:
            status = "INACTIVE"
        return status
    #end def

    @validates('item_title')
    def validate_item_title(self, item_title):
        # allow all character
        pattern = r"^[a-z-A-Z_0-9 ]+$"
        if len(item_title) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(item_title))
        if len(item_title) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(item_title))
        if  re.match(pattern, item_title) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(item_title))
    #end def

    @validates('description')
    def validate_description(self, description):
        # allow all characters except number
        pattern = r"."
        if len(description) < 2:
            raise ValidationError('Invalid description, min is 2 characters')
        if len(description) > 1000:
            raise ValidationError('Invalid description, min is 1000 character')
        if re.match(pattern,description) is None:
            raise ValidationError(' see the rule of description')

    @validates('price')
    def validate_price(self, price):
        # allow all character
        pattern = r"^[0-9]+$"
        if len(price) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(price))
        if len(price) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(price))
        if  re.match(pattern, price) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(price))
    #end def
