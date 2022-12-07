import logging

from flask import Flask
from huey import RedisHuey
from mongoengine import connect

from config import Config
from n3robot import (N3TelegramMessagePipeline, N3TelegramMessagePush, N3TelegramMessageBuild, N3TelegramMessageTagPush)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

app_logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)
huey = RedisHuey(host=app.config.get('REDIS_HOST'))

connect(
    db=app.config.get('MONGODB_DATABASE'),
    username=app.config.get('MONGODB_USER'),
    password=app.config.get('MONGODB_PASSWORD'),
    host=app.config.get('MONGODB_HOST'),
    authentication_source='admin'
)

gitlab_hook_map = {
    'Pipeline Hook': N3TelegramMessagePipeline,
    'Push Hook': N3TelegramMessagePush,
    'Job Hook': N3TelegramMessageBuild,
    'Tag Push Hook': N3TelegramMessageTagPush
}

emoji_map = {
    'success_emoji': '✅',
    'running_emoji': '🏃‍',
    'failed_emoji': '😱',
    'canceled_emoji': '🙅‍',
    'skipped_emoji': '😢',
    'commit_emoji': '🤝',
    'created_emoji': '💩',
    'tag_emoji': '➕',
}

from app import routes
