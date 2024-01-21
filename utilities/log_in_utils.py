from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import *
import os

def log_in_to_inventory(context, user, password):
    context.driver = webdriver.Chrome()
    context.driver.get(os.getenv('ROOT_URL'))
    context.driver.find_element(By.ID, 'user-name').send_keys(user)
    context.driver.find_element(By.ID, 'password').send_keys(password)
    context.driver.find_element(By.ID, 'login-button').click()
