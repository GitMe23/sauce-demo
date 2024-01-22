import os
import json
from dotenv import load_dotenv
load_dotenv(override=True)

# Password
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")

# Load user_list from the 
with open('fixtures/users.json', 'r') as data:
    users = json.load(data)
    user_list = users.get('user_list', [])

# Create a user dictionary
user_dict = {user.upper(): user for user in user_list}

# CSS ID selectors:
USER = "user-name"
PASSWORD = "password"
LOGIN = "login-button"
SHOPPING_CART = "shopping_cart_container"
CHECKOUT = "checkout"
FIRST_NAME = "first-name"
LAST_NAME = "last-name"
POST_CODE = "postal-code"

