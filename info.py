import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Admins & Channels
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(channel) if re.search('^-100\d+$', channel) else channel for channel in environ['CHANNELS'].split()]

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
<i>Hello I am @File2UX's Media Finder Bot</i>

<b>Here you can search files which are uploaded on @File2UX You Can Use This Bot In Inline</b>

<a href='https://t.me/File2UChat/1501'>Click This To Know How To Use This Bot</a>

IF Want To Request Any Movies or Series Use <a href='http://telegram.me/File2UReqbot?start'>This Bot</a>

"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
