import re

from marshmallow import Schema, fields, ValidationError, post_load, validates
from app.api.create_app import db


def cannot_be_blank(string):
    if not string:
        raise ValidationError(" Data cannot be blank")
#end def

class ProductSchema(Schema):
    id                  = fields.Int()
    file_title          = fields.String(required=True, validate=cannot_be_blank)
    # file_name           = fields.String(attribute="file_name")
    status_file         = fields.Method("bool_to_status")
    created_at          = fields.DateTime()
    updated_at          = fields.DateTime()
    deleted_at          = fields.DateTime()
    item                = fields.Int()
        
    
    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status_file != True:
            status = "INACTIVE"
        return status
    #end def

    @validates('file_title')
    def validate_file_title(self, file_title):
        # allow all character
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(file_title) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(file_title))
        if len(file_title) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(file_title))
        if  re.match(pattern, file_title) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(file_title))
    #end def

    
    # @validates('file_name')
    # def validate_file_name(self, file_name):
    #     # allow all character
    #     pattern = r"."
    #     if len(file_name) < 2:
    #         raise ValidationError('Invalid {}. min is 2 character'.format(self.file_name))
    #     if len(file_name) > 40:
    #         raise ValidationError('Invalid {}, max is 40 character'.format(self.file_name))
    #     if  re.match(pattern, file_name) is None:
    #         raise ValidationError('Invalid {}. only alphabet is allowed'.format(self.file_name))
    #end def



class UpdateProductSchema(Schema):
    # file_name               = fields.Str(required=True, validate=cannot_be_blank) 
    file_title              = fields.Str(required=True, validate=cannot_be_blank)
    
    
    @validates('file_title')
    def validate_file_title(self, file_title):
        # allow all character
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(file_title) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(file_title))
        if len(file_title) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(file_title))
        if  re.match(pattern, file_title) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(file_title))
    #end def

    
    # @validates('file_name')
    # def validate_file_name(self, file_name):
    #     # allow all character
    #     pattern = r"."
    #     if len(file_name) < 2:
    #         raise ValidationError('Invalid {}. min is 2 character'.format(self.file_name))
    #     if len(file_name) > 40:
    #         raise ValidationError('Invalid {}, max is 40 character'.format(self.file_name))
    #     if  re.match(pattern, file_name) is None:
    #         raise ValidationError('Invalid {}. only alphabet is allowed'.format(self.file_name))
    #end def
