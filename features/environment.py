from config.logging_config import *
from utilities import env_utils, utils

def before_all(context):
   logging.info('Running Behave...')
   env_utils.create_properties()

def before_scenario(context, scenario):
   if "browser" in scenario.tags:
      logging.info(f'Initialising web driver for {scenario}')
      context.driver = utils.initialise_driver()
      
def after_scenario(context, scenario):
    if "browser" in scenario.tags:
      logging.info(f'Quitting driver for {scenario}')
      context.driver.quit()

def after_step(context, step):
   if step.status == "failed":
    logging.warning(f'Step failed: {step}')

def after_feature(context, feature):
   logging.info(f'Finished: {feature}')

def after_all(context):
   logging.info('Behave finished')

