from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import *
import os
from utilities import utils


@given('I am on the Sauce Demo login page')
def step_open_swag_login_page(context):
    context.driver = utils.initialise_driver()
    utils.navigate_to_root(context.driver)

@when('I enter user name "{user}" and a valid password')
def step_when(context, user):
    utils.enter_credentials(context.driver, user, SAUCE_PASSWORD)

@when('I click the login button')
def step_click_login_button(context):
    context.driver.find_element(By.ID, 'login-button').click()

@then('I should be taken to the inventory page')
def step_then(context):
    expected_url = f"{os.getenv('ROOT_URL')}/inventory.html"
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

@given("I am on the inventory page")
def step_given(context):
    context.driver = utils.log_in_to_inventory(user_dict['STANDARD_USER'], SAUCE_PASSWORD)
    

