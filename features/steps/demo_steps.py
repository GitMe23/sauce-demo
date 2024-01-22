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

@when('I click "{id}"')
def step_click(context, id):
    utils.clickById(context.driver, id)

@then('I should be taken to the "{page_name}" page')
def step_then_inventory(context, page_name):
    expected_url = f"{os.getenv('ROOT_URL')}/{page_name}.html"
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

@given("I log on to the inventory page")
def step_given_inventory(context):
    utils.log_in_to_inventory(context.driver)

@given('I have a list of {items} to order') 
def step_given_list(context, items):
    context.items = [item.strip() for item in items.split(',')]

@when("I click 'Add to cart' for each item")
def step_when_add_to_cart(context):
    utils.add_items_to_cart(context.driver, context.items)

@then('I should see all of my items')
def step_see_items(context):
    results = [utils.item_is_in_cart(context, item) for item in context.items]
    assert all(results), "Not all items are in the cart"

@given('I am on the cart page')
def step_open_cart_page(context):
    utils.navigate_to_cart(context.driver, context.items)

@given('I am on the "checkout-step-one" page')
def step_open_checkout_stage_one(context):
    utils.navigate_to_checkout_step_one(context.driver, context.items)    

@given('I enter my {first} name, {last} name, and {postal_code}') 
def step_given_enter_details(context, first, last, postal_code): 
    utils.enter_user_details(context.driver, first, last, postal_code)  

@given('I am on the "checkout-step-two" page')
def step_open_checkout_step_two(context):
    utils.navigate_to_checkout_step_two(context.driver, context.items)  

@then('I should see "{text}"')
def step_then_see_message(context, text):
    utils.is_visible(context.driver, text)


     
    
    





    





