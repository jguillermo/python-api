from functools import wraps

from src.shared.exception import UnauthorizedRequest, BadRequest
from src.shared.infrastructure.response import Response


def handler_except(method):
    @wraps(method)
    def method_wrapper(*args, **kwargs):

        try:
            rpta = method(*args, **kwargs)
            return Response.success(rpta)
        except BadRequest as br:
            return Response.error(rpta)
        except Exception as e:
            resp.media = response.error(e.__str__())
            resp.status = falcon.HTTP_500

    return method_wrapper
