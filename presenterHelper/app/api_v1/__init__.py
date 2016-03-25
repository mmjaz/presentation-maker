from flask import Blueprint

api = Blueprint('api', __name__)


@api.before_request
def before_request():
    """All routes in this blueprint require authentication."""
    pass


@api.after_request
def after_request(rv):
    """Generate an ETag header for all routes in this blueprint."""
    return rv


from . import users