from __future__ import division
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse

from core.helpers.constants import RequestContentTypes

###### JSON API Response Helpers #######
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data: dict, **kwargs):
        content = JSONRenderer().render(data)
        kwargs["content_type"] = RequestContentTypes.APPLICATION_JSON
        super(JSONResponse, self).__init__(content, **kwargs)


class UnauthorizedJSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    Status code: 401 - Response for unauthorized access
    """

    def __init__(self, data: dict = None, message: str = None, **kwargs):
        payload = {"code": 401}
        if data:
            payload.update({"response": data})
        if message:
            payload.update({"message": message})
        content = JSONRenderer().render(payload)
        print(content)
        kwargs["content_type"] = RequestContentTypes.APPLICATION_JSON
        super(UnauthorizedJSONResponse, self).__init__(content, status=401, **kwargs)


class BadRequestJSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    Status code - 400, Response for bad request
    """

    def __init__(self, data: dict = None, message: str = None, status=400, **kwargs):
        payload = {"code": status}
        if data:
            payload.update({"response": data})
        if message:
            payload.update({"message": message})
        content = JSONRenderer().render(payload)
        print(content)
        kwargs["content_type"] = RequestContentTypes.APPLICATION_JSON
        super(BadRequestJSONResponse, self).__init__(content, status=status, **kwargs)


class NotFoundJSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    Status code - 404, Response for object not found
    """

    def __init__(
        self, data: dict = None, message: str = None, status_code=404, **kwargs
    ):
        payload = {"code": 404}
        if data:
            payload.update({"response": data})
        if message:
            payload.update({"message": message})
        content = JSONRenderer().render(payload)
        print(content)
        kwargs["content_type"] = RequestContentTypes.APPLICATION_JSON
        super(NotFoundJSONResponse, self).__init__(
            content, status=status_code, **kwargs
        )


class ForbiddenJSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    Status code - 403, Response for forbidden operation
    """

    def __init__(self, data: dict = None, message: str = None, **kwargs):
        payload = {"code": 403}
        if data:
            payload.update({"response": data})
        if message:
            payload.update({"message": message})
        content = JSONRenderer().render(payload)
        print(content)
        kwargs["content_type"] = RequestContentTypes.APPLICATION_JSON
        super(ForbiddenJSONResponse, self).__init__(content, status=403, **kwargs)


class ServerErrorJSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    Status code - 500, Response for internal server error
    """

    def __init__(self, data: dict = None, message: str = None, **kwargs):
        payload = {"code": 500}
        if data:
            payload.update({"response": data})
        if message:
            payload.update({"message": message})
        content = JSONRenderer().render(payload)
        print(content)
        kwargs["content_type"] = RequestContentTypes.APPLICATION_JSON
        super(ServerErrorJSONResponse, self).__init__(content, status=500, **kwargs)


class SuccessJSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    Status code - 200, Response for successful completion of request
    """

    def __init__(self, data=None, message=None, **kwargs):
        payload = {"code": 200}
        if data:
            payload.update({"response": data})
        if message:
            payload.update({"message": message})
        content = JSONRenderer().render(payload)
        print(content)
        kwargs["content_type"] = RequestContentTypes.APPLICATION_JSON
        super(SuccessJSONResponse, self).__init__(content, status=200, **kwargs)
