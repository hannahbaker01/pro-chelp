import os
import loguru
from urllib.parse import quote_plus
import re

def format_mangodb(uri):
    pattern = re.compile(r'mongodb\+srv://([^:]+):([^@]+)@([^/]+)(/[^?]+)?(\?.*)?')
    match = pattern.search(uri)
    if not match:
        raise ValueError("Invalid URI format.")
    
    username, password, host, path, query = match.groups()
    encoded_uri = f'mongodb+srv://{quote_plus(username)}:{quote_plus(password)}@{host}{path or ""}{query or ""}'
    return encoded_uri

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)
LOGGER = loguru.logger
if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    OWNER_ID = os.environ.get('OWNER_ID', 6258709129)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    MONGO_URL = os.environ.get('MONGO_URL', None)
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = ... # api id here
    OWNER_ID = ...
    API_HASH = "api hash"
    BOT_TOKEN = "bot token"
    MONGO_URL = "here mango url"
    MUST_JOIN = "OldLostFriends" # must join channel link here
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
