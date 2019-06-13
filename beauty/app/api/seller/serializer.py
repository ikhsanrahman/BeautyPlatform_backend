import re

from marshmallow import Schema, fields, ValidationError, post_load, validates
from app.api.create_app import db


def cannot_be_blank(string):
    if not string:
        raise ValidationError(" Data cannot be blank")
#end def

class SellerSchema(Schema):
    id                  = fields.Int()
    full_name           = fields.String(required=True, validate=cannot_be_blank)
    email               = fields.Email(required=True, validate=cannot_be_blank)
    password            = fields.String(required=True, validate=cannot_be_blank)
    password_hash       = fields.String(attribute="password_hash")
    gender              = fields.String(required=True, validate=cannot_be_blank)
    phone_number        = fields.String(required=True, validate=cannot_be_blank)
    status_seller       = fields.Method("bool_to_status")
    created_at          = fields.DateTime()
    updated_at          = fields.DateTime()
    deleted_at          = fields.DateTime()
    # video            = fields.String(load_only)
    # paper            = fields
        
    
    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status_seller != True:
            status = "INACTIVE"
        return status
    #end def

    @validates('full_name')
    def validate_full_name(self, full_name):
        # allow all character
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(full_name) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(self.full_name))
        if len(full_name) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(self.full_name))
        if  re.match(pattern, full_name) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(self.full_name))
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
            raise ValidationError('Invalid {}. min is 2 character'.format(self.phone_number))
        if len(phone_number) > 40:
            raise ValidationError('Invalid {}}, max is 40 character'.format(self.phone_number))
        if  re.match(pattern, phone_number) is None:
            raise ValidationError('Invalid {}}. only alphabet is allowed'.format(self.phone_number))
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

    # @validates('major')
    # def validate_major(self, major):
    #     # allow all characters except number

    #     pattern = r"^[a-z-A-Z_ ]+$"
    #     if len(major) < 2:
    #         raise ValidationError('Invalid alamat')
    #     if len(major) > 20:
    #         raise ValidationError('Invalid alamat, max is 20 character')
    #     if  re.match(pattern, major) is None:
    #         raise ValidationError('Invalid alamat, only Human allowed to create the field, not you')

    # @validates('interesting_field')
    # def validate_interesting_field(self, interesting_field):
    #     # allow all character
    #     pattern = r"^[a-z-A-Z_ ]+$"
    #     if len(interesting_field) < 2:
    #         raise ValidationError('Invalid category. min is 2 character')
    #     if len(interesting_field) > 40:
    #         raise ValidationError('Invalid category, max is 40 character')
    #     if  re.match(pattern, interesting_field) is None:
    #         raise ValidationError('Invalid category. only alphabet is allowed')
    # #end def

    # @validates('university')
    # def validate_university(self, university):
    #     # allow all characters except number

    #     pattern = r"^[a-z-A-Z_ ]+$"
    #     if len(university) < 2:
    #         raise ValidationError('Invalid universitas')
    #     if len(university) > 20:
    #         raise ValidationError('Invalid universitas, max is 20 character')
    #     if  re.match(pattern, university) is None:
    #         raise ValidationError('Invalid universitas, only Human allowed to create the field, not you')
    # #end def

class LoginSellerSchema(Schema):
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


class UpdateSellerSchema(Schema):
    full_name               = fields.Str(required=True, validate=cannot_be_blank) 
    phone_number            = fields.Str(required=True, validate=cannot_be_blank)
    gender                  = fields.Str(required=True, validate=cannot_be_blank)
    
    
    @validates('full_name')
    def validate_full_name(self, full_name):
        # allow all character
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(full_name) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(self.full_name))
        if len(full_name) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(self.full_name))
        if  re.match(pattern, full_name) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(self.full_name))
    #end def

    @validates('phone_number')
    def validate_phone_number(self, phone_number):
        # allow all character
        pattern = r"^[0-9]+$"
        if len(phone_number) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(self.phone_number))
        if len(phone_number) > 40:
            raise ValidationError('Invalid {}}, max is 40 character'.format(self.phone_number))
        if  re.match(pattern, phone_number) is None:
            raise ValidationError('Invalid {}}. only alphabet is allowed'.format(self.phone_number))
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

    # @validates('major')
    # def validate_major(self, major):
    #     # allow all characters except number

    #     pattern = r"^[a-z-A-Z_ ]+$"
    #     if len(major) < 2:
    #         raise ValidationError('Invalid alamat')
    #     if len(major) > 20:
    #         raise ValidationError('Invalid alamat, max is 20 character')
    #     if  re.match(pattern, major) is None:
    #         raise ValidationError('Invalid alamat, only Human allowed to create the field, not you')


    # @validates('university')
    # def validate_university(self, university):
    #     # allow all characters except number

    #     pattern = r"^[a-z-A-Z_ ]+$"
    #     if len(university) < 2:
    #         raise ValidationError('Invalid universitas')
    #     if len(university) > 20:
    #         raise ValidationError('Invalid universitas, max is 20 character')
    #     if  re.match(pattern, university) is None:
    #         raise ValidationError('Invalid universitas, only Human allowed to create the field, not you')
    # #end def

    # @validates('interesting_field')
    # def validate_interesting_field(self, interesting_field):
    #     # allow all character
    #     pattern = r"^[a-z-A-Z_ ]+$"
    #     if len(interesting_field) < 2:
    #         raise ValidationError('Invalid category. min is 2 character')
    #     if len(interesting_field) > 40:
    #         raise ValidationError('Invalid category, max is 40 character')
    #     if  re.match(pattern, interesting_field) is None:
    #         raise ValidationError('Invalid category. only alphabet is allowed')
    # #end def

class UpdatePasswordSchema(Schema):
    new_password            = fields.Str(required=True, validate=cannot_be_blank)
    confirm_new_password    = fields.Str(required=True, validate=cannot_be_blank)

class ForgetPasswordSchema(Schema):
    new_password            = fields.Str(required=True, validate=cannot_be_blank)
    confirm_new_password    = fields.Str(required=True, validate=cannot_be_blank)
