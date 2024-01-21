from behave import fixture
from utilities.utils import initialise_driver

def before_all(context):
   print('Before all executed')

def before_scenario(scenario, context):
    print('Before scenario executed')

def after_scenario(scenario, context):
    print('After scenario executed')

def after_feature(scenario, context):
   print('After feature executed')

def after_all(context):
        print('after all')
        