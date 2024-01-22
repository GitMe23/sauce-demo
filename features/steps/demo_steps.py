from behave import *
from selenium.webdriver.common.by import By
from config.config import *
import os
from utilities import utils
from config.logging_config import *

@given('I am on the Sauce Demo login page')
def step_open_swag_login_page(context):
    utils.navigate_to_root(context.driver)

@when('I enter user name "{user}" and a valid password')
def step_when_log_in(context, user):
    utils.enter_credentials(context.driver, user, SAUCE_PASSWORD)

@when('I click the "{id}"')
def step_click(context, id):
    context.driver.find_element(By.ID, id).click()

@then('I should be taken to the inventory page')
def step_then_inventory(context):
    expected_url = f"{os.getenv('ROOT_URL')}/inventory.html"
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

@given("I log on to the inventory page")
def step_given_inventory(context):
    utils.log_in_to_inventory(context.driver)

@given("I have a list of '{items}' to order") 
def step_given_list(context, items):
    context.items = [item.strip() for item in items.split(',')]

@when("I click 'Add to cart' for each item")
def step_when_add_to_cart(context):
    for item in context.items:
        item_id = f'add-to-cart-{item.lower().replace(" ", "-")}'
        utils.clickById(context.driver, item_id)
        

    





