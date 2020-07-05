from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.cache import patch_response_headers
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, never_cache
from django.views.decorators.csrf import csrf_exempt


class HttpResponseMixin(object):
    is_json = False

    def render_to_response(self, data, status=200):
        content_type = 'text/html'
        if self.is_json:
            content_type = 'application/json' 
        return HttpResponse(data, content_type=content_type, status=status)


class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context

# class NeverCacheMixin(object):
#     @method_decorator(never_cache)
#     def dispatch(self, *args, **kwargs):
#         return super(NeverCacheMixin, self).dispatch(*args, **kwargs)


# class LoginRequiredMixin(object):
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


# class CSRFExemptMixin(object):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, *args, **kwargs):
#         return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)


# class CacheMixin(object):
#     cache_timeout = 60

#     def get_cache_timeout(self):
#         return self.cache_timeout

#     def dispatch(self, *args, **kwargs):
#         return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)


# class CacheControlMixin(object):
#     cache_timeout = 60

#     def get_cache_timeout(self):
#         return self.cache_timeout

#     def dispatch(self, *args, **kwargs):
#         response = super(CacheControlMixin, self).dispatch(*args, **kwargs)
#         patch_response_headers(response, self.get_cache_timeout())
#         return response


# class JitterCacheMixin(CacheControlMixin):
#     cache_range = [40, 80]

#     def get_cache_range(self):
#         return self.cache_range

#     def get_cache_timeout(self):
#         return random.randint(*self.get_cache_range())
