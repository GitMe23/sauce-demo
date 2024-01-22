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
    enter_credentials(driver, user_dict['STANDARD_USER'], SAUCE_PASSWORD)
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

def navigate_to_checkout_step_two(driver, items, first, last, area_code):
    navigate_to_checkout_step_one(driver, items)
    enter_user_details(driver, first, last, area_code)

def enter_user_details(driver, first, last, postal_code):
    driver.find_element(By.ID, FIRST_NAME).send_keys(first)
    driver.find_element(By.ID, LAST_NAME).send_keys(last)
    driver.find_element(By.ID, POST_CODE).send_keys(postal_code)





