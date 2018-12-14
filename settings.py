from datetime import timedelta

class Config():
    ENV=None,
    DEBUG=False,
    TESTING=False,
    PROPAGATE_EXCEPTIONS=None,
    PRESERVE_CONTEXT_ON_EXCEPTION=None,
    SECRET_KEY=None,
    PERMANENT_SESSION_LIFETIME=timedelta(days=31),
    USE_X_SENDFILE=False,
    #SERVER_NAME="www.caochen.com",
    APPLICATION_ROOT='/',
    SESSION_COOKIE_NAME='session',
    SESSION_COOKIE_DOMAIN=None,
    SESSION_COOKIE_PATH=None,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_SAMESITE=None,
    SESSION_REFRESH_EACH_REQUEST=True,
    MAX_CONTENT_LENGTH=None,
    SEND_FILE_MAX_AGE_DEFAULT=timedelta(hours=12),
    TRAP_BAD_REQUEST_ERRORS=None,
    TRAP_HTTP_EXCEPTIONS=False,
    EXPLAIN_TEMPLATE_LOADING=False,
    PREFERRED_URL_SCHEME='http',
    JSON_AS_ASCII=True,
    JSON_SORT_KEYS=True,
    JSONIFY_PRETTYPRINT_REGULAR=False,
    JSONIFY_MIMETYPE='application/json',
    TEMPLATES_AUTO_RELOAD=None,
    MAX_COOKIE_SIZE=4093,

class ProductionConfig(Config):
    DEBUG=False

class DevelopementConfig(Config):
    DEBUG=True