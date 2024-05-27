import time
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse


class RateLimitMiddleware:
    """
    RateLimitMiddleware provides basic protection against DDoS attacks by
    limiting the number of requests from one IP address during a given period
    of time. If the number of requests exceeds the limit normal, the IP address
    is blocked for a certain time.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = settings.RATE_LIMIT

    def __call__(self, request):
        ip = self.get_client_ip(request)

        # Checking if the IP is blocked
        if self.is_blocked(ip):
            return JsonResponse({"error": "IP temporarily blocked"}, status=403)

        # Checking the request limit
        if self.is_rate_limited(ip):
            self.block_ip(ip)
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

        # Storing keys with a timeout equal to the time period for restricting requests
        cache.set(cache_key, request_times,
                  timeout=self.rate_limit["TIME_PERIOD"])

        # Login to verify installation of keys
        print(f"Set cache key {cache_key} with values {request_times}")

        return len(request_times) > self.rate_limit["MAX_REQUESTS"]

    def block_ip(self, ip):
        # Block the IP for a certain time
        block_time = self.rate_limit.get("BLOCK_TIME", 600)
        cache.set(f"blocked_{ip}", True, timeout=block_time)

        # Additional logging
        print(f"Blocked IP {ip} for {block_time} seconds")

    def is_blocked(self, ip):
        return cache.get(f"blocked_{ip}", False)
