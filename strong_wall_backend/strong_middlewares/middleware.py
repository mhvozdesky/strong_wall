import time
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = settings.RATE_LIMIT

    def __call__(self, request):
        ip = self.get_client_ip(request)
        if self.is_rate_limited(ip):
            return JsonResponse({"error": "Too many requests"}, status=429)

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def is_rate_limited(self, ip):
        current_time = time.time()
        cache_key = f"rate_limit_{ip}"
        request_times = cache.get(cache_key, [])

        # clearing old records
        request_times = [timestamp for timestamp in request_times if
                         current_time - timestamp < self.rate_limit[
                             "TIME_PERIOD"]]
        request_times.append(current_time)

        cache.set(cache_key, request_times,
                  timeout=self.rate_limit["TIME_PERIOD"])

        return len(request_times) > self.rate_limit["MAX_REQUESTS"]
