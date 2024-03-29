import os
import json
from dotenv import load_dotenv
load_dotenv(override=True)

# Password
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")

# CSS ID selectors:
USER = "user-name"
PASSWORD = "password"
LOGIN = "login-button"
SHOPPING_CART = "shopping_cart_container"
CHECKOUT = "checkout"
FIRST_NAME = "first-name"
LAST_NAME = "last-name"
POST_CODE = "postal-code"
CONTINUE = "continue"

# Load user_list from test fixtures
with open('fixtures/users.json', 'r') as data:
    users = json.load(data)
    user_list = users.get('user_list', [])

# Create a user dictionary
USER_DICT = {user.upper(): user for user in user_list}

# Path to test fixtures
ITEMS = 'fixtures/items.json'




