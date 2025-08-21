from decouple import config

ENV = config('ENVIRONMENT', default='dev')

if ENV == 'prod':
    from .prod import *
else:
    from .dev import *