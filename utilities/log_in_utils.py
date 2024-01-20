from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import *
import os
from dotenv import load_dotenv
load_dotenv(override=True)  

def log_in(context, user, password):
    context.driver.find_element(By.ID, 'user-name').send_keys(user)
    context.driver.find_element(By.ID, 'password').send_keys(password)
