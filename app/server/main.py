from .monitoring import enable_sentry
from config import environment
from api import server as app

enable_sentry(environment.sentry)

