from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *
import os
from dotenv import load_dotenv
load_dotenv(override=True)  

@given('I open the Sauce Demo login page')
def step_open_swag_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com")

@when('I enter a valid user name and password')
def step_enter_valid_credentials(context):
    context.driver.find_element(By.ID, 'user-name').send_keys(user_dict['STANDARD_USER'])
    context.driver.find_element(By.ID, 'password').send_keys(os.getenv('SAUCE_PASSWORD'))

@when('I click the login button')
def step_click_login_button(context):
    context.driver.find_element(By.ID, 'login-button').click()

@then('I should be on the inventory page')
def step_then(context):
    expected_url = f"{os.getenv('ROOT_URL')}/inventory.html"
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"
