from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config.config import *
import os
from utilities import utils
import pandas as pd
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


@then('I should see that the total price is the correct sum of chosen items')
def step_items_sum(context):
    swag_catalogue_df = pd.read_json(ITEMS, orient='columns')
    items_to_sum = context.items
    
    # Filter the catalogue for user's items
    filtered_df = swag_catalogue_df[swag_catalogue_df['name'].isin(items_to_sum)]
   
    # Calculate the sum of prices for the specified items
    expected_total = filtered_df['price'].sum()
    logging.info(f'\nChosen items:\n{filtered_df}\n EXPECTED TOTAL: ${expected_total}')
    
    # Get total on page
    actual_total = utils.get_item_total_on_page(context.driver)

    assert actual_total == expected_total, f'ACTUAL TOTAL: {actual_total}, EXPECTED TOTAL: {expected_total}'
    

@when('I double click on the quantity of an item')
def step_click_quantity(context):
    wait = WebDriverWait(context.driver, 1)
    context.cart_quantity_div = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'cart_quantity')))
    actions = ActionChains(context.driver)
    actions.double_click(context.cart_quantity_div).perform()

@then('I should be able to enter a new {value}')
def step_enter_qty(context, value):
    assert context.cart_quantity_div.send_keys(value), f"Failed to enter a new value: {value}"









     
    
    





    





