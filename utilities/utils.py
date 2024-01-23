from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import *
import os
from config.logging_config import *
from bs4 import BeautifulSoup

def initialise_driver():
    return webdriver.Chrome()

def navigate_to_root(driver):
    driver.get(os.getenv('ROOT_URL'))

def enter_credentials(driver, user, password):
    driver.find_element(By.ID, USER).send_keys(user)
    driver.find_element(By.ID, PASSWORD).send_keys(password)

def clickById(driver, element_id):
    driver.find_element(By.ID, element_id).click()

def log_in_to_inventory(driver):
    navigate_to_root(driver)
    enter_credentials(driver, USER_DICT['STANDARD_USER'], SAUCE_PASSWORD)
    clickById(driver, LOGIN)
    return driver

def add_items_to_cart(driver, items):
    for item in items:
        item_id = f'add-to-cart-{item.lower().replace(" ", "-")}'
        clickById(driver, item_id)

def item_is_in_cart(context, item_name):
    html_content = context.driver.page_source    
    soup = BeautifulSoup(html_content, 'html.parser')
    inventory_item_div = soup.find('div', class_='inventory_item_name', string=item_name)
    return inventory_item_div is not None

def navigate_to_cart(driver, items):
    log_in_to_inventory(driver) 
    add_items_to_cart(driver, items) 
    clickById(driver, SHOPPING_CART) 

def navigate_to_checkout_step_one(driver, items):
    navigate_to_cart(driver, items)
    clickById(driver, CHECKOUT)

def navigate_to_checkout_step_two(driver, items, first="P.A.", last="Consulting", postal_code="EC1M 3HE"):
    navigate_to_checkout_step_one(driver, items)
    enter_user_details(driver, first, last, postal_code)
    clickById(driver, CONTINUE)

def enter_user_details(driver, first, last, postal_code):
    driver.find_element(By.ID, FIRST_NAME).send_keys(first)
    driver.find_element(By.ID, LAST_NAME).send_keys(last)
    driver.find_element(By.ID, POST_CODE).send_keys(postal_code)

def is_visible(driver, text):
    soup = get_html_content(driver)
    elements_with_text = soup.find_all(string=text)
    visible_elements = [element for element in elements_with_text if element.parent and element.parent.visible]
    return bool(visible_elements)    

def get_item_total_on_page(driver):
    soup = get_html_content(driver)
    subtotal_div = soup.find('div', class_='summary_subtotal_label')
    
    if subtotal_div:
        subtotal_text = subtotal_div.get_text(strip=True)
        prefix = "Item total: $"
        
        if prefix in subtotal_text:
            item_total = float(subtotal_text.split(prefix)[1].replace(',', '').strip())
            return item_total
    
    return None

def get_html_content(driver):
    html_content = driver.page_source    
    return BeautifulSoup(html_content, 'html.parser')

def get_number_of_items_on_cart_badge(driver):
    html_content = get_html_content(driver)
    cart_badge_span = html_content.find('span', class_='shopping_cart_badge')
    if cart_badge_span:
        cart_badge_text = cart_badge_span.get_text(strip=True)
        try:
            number_of_items_in_cart = int(cart_badge_text)
            return number_of_items_in_cart
        except ValueError:
            logging.warning(f'Failed to convert cart badge text to integer: {cart_badge_text}')
            return 0
    else:
        return 0


def get_remove_button(driver, item):
    get_html_content(driver)
    item_id = f'remove-{item.lower().replace(" ", "-")}'    
    remove_button = driver.find_element(By.ID, item_id)
    return remove_button

