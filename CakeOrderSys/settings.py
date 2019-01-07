from datetime import timedelta
import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

class BaseConfig():
    ENV=None,
    DEBUG=False,
    TESTING=False,
    PROPAGATE_EXCEPTIONS=None,
    PRESERVE_CONTEXT_ON_EXCEPTION=None,
    SECRET_KEY=None,
    # PERMANENT_SESSION_LIFETIME=timedelta(days=31),
    # USE_X_SENDFILE=False,
    # SERVER_NAME="www.caochen.com",
    # APPLICATION_ROOT='/',
    # SESSION_COOKIE_NAME='session',
    # SESSION_COOKIE_DOMAIN=None,
    # SESSION_COOKIE_PATH=None,
    # SESSION_COOKIE_HTTPONLY=True,
    # SESSION_COOKIE_SECURE=False,
    # SESSION_COOKIE_SAMESITE=None,
    # SESSION_REFRESH_EACH_REQUEST=True,
    # MAX_CONTENT_LENGTH=None,
    # SEND_FILE_MAX_AGE_DEFAULT=timedelta(hours=12),
    # TRAP_BAD_REQUEST_ERRORS=None,
    # TRAP_HTTP_EXCEPTIONS=False,
    # EXPLAIN_TEMPLATE_LOADING=True,
    # PREFERRED_URL_SCHEME='http',
    # JSON_AS_ASCII=True,
    # JSON_SORT_KEYS=True,
    # JSONIFY_PRETTYPRINT_REGULAR=False,
    # JSONIFY_MIMETYPE='application/json',
    # TEMPLATES_AUTO_RELOAD=None,
    # MAX_COOKIE_SIZE = 4093,
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = os.urandom(24)

class DevelopementConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = "caochen520"
    PREFERRED_URL_SCHEME = 'https',
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')
    print(SQLALCHEMY_DATABASE_URI)
    
config = {
    'development': DevelopementConfig,
    'production': ProductionConfig,
}