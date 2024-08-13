import os
from configparser import ConfigParser



config = ConfigParser()
config.read("config.ini")


bot_token = os.getenv('bot_token',
                      config.get('bot', 'token', fallback=None))

if not bot_token:
    exit('please, provide bot_token env variable')

