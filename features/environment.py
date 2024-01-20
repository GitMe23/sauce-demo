from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import *
import os
from dotenv import load_dotenv
load_dotenv(override=True) 

def before_all(context):
   print('Before all executed')

def before_scenario(scenario, context):
    print('Before scenario executed')

def after_feature(scenario, context):
   print('After feature executed')

def after_all(context):
        print('Closed Chrome driver')