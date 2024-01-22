from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import *
import os
import logging as log

def initialise_driver():
    return webdriver.Chrome()

def navigate_to_root(driver):
    driver.get(os.getenv('ROOT_URL'))

def enter_credentials(driver, user, password):
    driver.find_element(By.ID, 'user-name').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)

def clickById(driver, element_id):
    driver.find_element(By.ID, element_id).click()

def log_in_to_inventory():
    driver = initialise_driver()
    navigate_to_root(driver)
    enter_credentials(driver, user_dict['STANDARD_USER'], SAUCE_PASSWORD)
    clickById(driver, "login-button")
    return driver

def get_item_container(context, item_name):
    # Find the div with class 'inventory_item' that contains a div with class 
    # 'inventory_item_name' equal to the current item
    css_selector = f'div.inventory_item:has(div.inventory_item_name:contains("{item_name}"))'
    inventory_item_div = context.driver.find_element_by_css_selector(css_selector)
    return inventory_item_div