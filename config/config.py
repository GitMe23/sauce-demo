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
LOGIN = "login-button"
CART = "cart_contents_container"

