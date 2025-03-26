# middleware.py
from django.http import HttpResponseRedirect
from urllib.parse import urlparse, urlunparse

class FixTestCASRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        full_path = request.get_full_path()
        
        if full_path.count('?') > 1:
            path, first_qmark, rest = full_path.partition('?')
            # Replace all subsequent '?' with '&'
            fixed_rest = rest.replace('?', '&')
            fixed_url = f"{path}?{fixed_rest}"

            return HttpResponseRedirect(fixed_url)

        response = self.get_response(request)
        return response
