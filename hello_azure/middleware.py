from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info("JEREVOSS: HealthCheckMiddleware.call()")
        if request.path == "/api/health":
            return HttpResponse("ok\n")
        return self.get_response(request)
    