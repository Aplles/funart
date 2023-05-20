import sys

from rest_framework.response import Response


def custom_exception_handler(exc, context):
    try:
        response_status = exc.response_status
    except AttributeError:
        response_status = 500
    return Response({sys.exc_info()[0].__name__: exc.__str__()}, status=response_status)
