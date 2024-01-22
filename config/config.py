# Password(s)
import os
from dotenv import load_dotenv
from fixtures import users
load_dotenv(override=True)
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")

# Users
user_dict = {user.upper(): user for user in users.user_list}

# CSS ID selectors:
LOGIN = "login-button"

