from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

class BaseError:

	def errResponse(status_code, message=None):
	    error = {}

	    if message:
	        error["errors"] = message
	    else:
	        error["errors"] = HTTP_STATUS_CODES.get(status_code, 'Unknown Error'),
	    #end if
	    return error, status_code

class SellerError(BaseError):
    def requestSuccess(message=None):
        return BaseError.errResponse(200, message)

    def badRequest(message=None):
        return BaseError.errResponse(400, message)

    def requestFailed(message=None):
        return BaseError.errResponse(401, message)

class ItemError(BaseError):
    def requestSuccess(message=None):
        return BaseError.errResponse(200, message)

    def badRequest(message=None):
        return BaseError.errResponse(400, message)

    def requestFailed(message=None):
        return BaseError.errResponse(401, message)

class ProductError(BaseError):
    def requestSuccess(message=None):
        return BaseError.errResponse(200, message)

    def badRequest(message=None):
        return BaseError.errResponse(400, message)

    def requestFailed(message=None):
        return BaseError.errResponse(401, message)

class BuyerError(BaseError):
    def requestSuccess(message=None):
        return BaseError.errResponse(200, message)

    def badRequest(message=None):
        return BaseError.errResponse(400, message)

    def requestFailed(message=None):
        return BaseError.errResponse(401, message)


