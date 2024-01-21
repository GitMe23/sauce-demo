from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import *
import os

def initialise_driver():
    return webdriver.Chrome()

def navigate_to_root(driver):
    driver.get(os.getenv('ROOT_URL'))

def enter_credentials(driver, user, password):
    driver.find_element(By.ID, 'user-name').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)

def click_login_button(driver):
    driver.find_element(By.ID, 'login-button').click()

def log_in_to_inventory(user, password):
    driver = initialise_driver()
    navigate_to_root(driver)
    enter_credentials(driver, user, password)
    click_login_button(driver)
    return driver
