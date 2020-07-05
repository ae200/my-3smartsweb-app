CORS_URLS_REGEX = r'^/api/.*$' # CORS HEADERS ENBALED
CORS_ORIGIN_WHITELIST = (
    "http://localhost:8000",
    'http://127.0.0.1'
)

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + ('X-CSRFToken', 'csrftoken',
    'content-type')

CORS_ALLOW_CREDENTIALS = True