import re

from marshmallow import Schema, fields, ValidationError, post_load, validates
from app.api.create_app import db


def cannot_be_blank(string):
    if not string:
        raise ValidationError(" Data cannot be blank")
#end def

class BuyerSchema(Schema):
    id                  = fields.Int()
    full_name           = fields.String(required=True, validate=cannot_be_blank)
    email               = fields.Email(required=True, validate=cannot_be_blank)
    password            = fields.String(required=True, validate=cannot_be_blank)
    password_hash       = fields.String(attribute="password_hash")
    gender              = fields.String(required=True, validate=cannot_be_blank)
    phone_number        = fields.String(required=True, validate=cannot_be_blank)
    address             = fields.String(required=True, validate=cannot_be_blank)
    status_seller       = fields.Method("bool_to_status")
    created_at          = fields.DateTime()
    updated_at          = fields.DateTime()
    deleted_at          = fields.DateTime()
    # video            = fields.String(load_only)
    # paper            = fields
        
    
    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status_buyer != True:
            status = "INACTIVE"
        return status
    #end def

    @validates('full_name')
    def validate_full_name(self, full_name):
        # allow all character
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(full_name) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(full_name))
        if len(full_name) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(full_name))
        if  re.match(pattern, full_name) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(full_name))
    #end def

    @validates('password')
    def validate_password(self, password):
        # allow all characters except number
        pattern = r"."
        if len(password) < 2:
            raise ValidationError('Invalid password, min is 2 characters')
        if len(password) > 40:
            raise ValidationError('Invalid password, min is 40 character')
        if re.match(pattern, password) is None:
            raise ValidationError('options can not be number at all. see the rule of options')

    @validates('phone_number')
    def validate_phone_number(self, phone_number):
        # allow all character
        pattern = r"^[0-9]+$"
        if len(phone_number) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(phone_number))
        if len(phone_number) > 40:
            raise ValidationError('Invalid {}}, max is 40 character'.format(phone_number))
        if  re.match(pattern, phone_number) is None:
            raise ValidationError('Invalid {}}. only alphabet is allowed'.format(phone_number))
    #end def

    @validates('gender')
    def validate_gender(self, gender):
        # only allow alphabet character and space
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(gender) < 2:
            raise ValidationError('Invalid gender')
        if len(gender) > 20:
            raise ValidationError('Invalid gender, max is 20 character')
        if  re.match(pattern, gender) is None:
            raise ValidationError('Invalid gender, only Human allowed to create the field, not you')
    #end def

    @validates('address')
    def validate_address(self, address):
        # allow all characters except number
        pattern = r"."
        if len(address) < 2:
            raise ValidationError('Invalid address, min is 2 characters')
        if len(address) > 40:
            raise ValidationError('Invalid address, min is 40 character')
        if re.match(pattern, address) is None:
            raise ValidationError('see the rule of address')


class LoginBuyerSchema(Schema):
    email               = fields.Email(required=True, validate=cannot_be_blank)
    password            = fields.String(required=True, validate=cannot_be_blank)

    @validates('password')
    def validate_password(self, password):
        # allow all characters except number
        pattern = r"."
        if len(password) < 2:
            raise ValidationError('Invalid password, min is 2 characters')
        if len(password) > 40:
            raise ValidationError('Invalid password, min is 40 character')
        if re.match(pattern, password) is None:
            raise ValidationError('options can not be number at all. see the rule of options')


class UpdateBuyerSchema(Schema):
    full_name               = fields.Str(required=True, validate=cannot_be_blank) 
    phone_number            = fields.Str(required=True, validate=cannot_be_blank)
    gender                  = fields.Str(required=True, validate=cannot_be_blank)
    address                 = fields.Str(required=True, validate=cannot_be_blank)

    
    @validates('full_name')
    def validate_full_name(self, full_name):
        # allow all character
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(full_name) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(full_name))
        if len(full_name) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(full_name))
        if  re.match(pattern, full_name) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(full_name))
    #end def

    @validates('phone_number')
    def validate_phone_number(self, phone_number):
        # allow all character
        pattern = r"^[0-9]+$"
        if len(phone_number) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(phone_number))
        if len(phone_number) > 40:
            raise ValidationError('Invalid {}}, max is 40 character'.format(phone_number))
        if  re.match(pattern, phone_number) is None:
            raise ValidationError('Invalid {}}. only alphabet is allowed'.format(phone_number))
    #end def

    @validates('gender')
    def validate_gender(self, gender):
        # only allow alphabet character and space
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(gender) < 2:
            raise ValidationError('Invalid gender')
        if len(gender) > 20:
            raise ValidationError('Invalid gender, max is 20 character')
        if  re.match(pattern, gender) is None:
            raise ValidationError('Invalid gender, only Human allowed to create the field, not you')
    #end def

    @validates('address')
    def validate_address(self, address):
        # allow all characters except number
        pattern = r"."
        if len(address) < 2:
            raise ValidationError('Invalid address, min is 2 characters')
        if len(address) > 40:
            raise ValidationError('Invalid address, min is 40 character')
        if re.match(pattern, address) is None:
            raise ValidationError('see the rule of address')


class UpdatePasswordSchema(Schema):
    new_password            = fields.Str(required=True, validate=cannot_be_blank)
    confirm_new_password    = fields.Str(required=True, validate=cannot_be_blank)

class ForgetPasswordSchema(Schema):
    new_password            = fields.Str(required=True, validate=cannot_be_blank)
    confirm_new_password    = fields.Str(required=True, validate=cannot_be_blank)
