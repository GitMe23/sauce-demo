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
    driver.find_element(By.ID, 'user-name').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)

def clickById(driver, element_id):
    driver.find_element(By.ID, element_id).click()

def log_in_to_inventory(driver):
    navigate_to_root(driver)
    enter_credentials(driver, user_dict['STANDARD_USER'], SAUCE_PASSWORD)
    clickById(driver, LOGIN)
    return driver

def item_is_in_cart(context, item_name):
    html_content = context.driver.page_source    
    soup = BeautifulSoup(html_content, 'html.parser')
    inventory_item_div = soup.find('div', class_='inventory_item_name', string=item_name)
    return inventory_item_div is not None