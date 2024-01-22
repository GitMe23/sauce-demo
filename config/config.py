# Password(s)
import os
from dotenv import load_dotenv
load_dotenv(override=True)
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")

# Users
user_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
user_dict = {user.upper(): user for user in user_list}

# CSS selectors:
