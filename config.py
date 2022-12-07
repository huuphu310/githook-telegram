from decouple import config


class Config(object):
    TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', default='')
    PROJECT_URL = config('PROJECT_URL', 'http://127.0.0.1')
    WIKI_URL = config('WIKI_URL', '')

    MONGODB_DATABASE = config('MONGODB_DATABASE', 'n3robot')
    MONGODB_USER = config('MONGODB_USER', 'n3robot')
    MONGODB_PASSWORD = config('MONGODB_PASSWORD')
    MONGODB_HOST = config('MONGODB_HOST', '127.0.0.1')
    REDIS_HOST = config('REDIS_HOST', '127.0.0.1')
