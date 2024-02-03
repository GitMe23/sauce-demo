import json
import os
from dotenv import load_dotenv
load_dotenv(override=True)

def create_properties():
    write_environment()
    write_executor()
    write_categories()

def write_environment():
    properties_path = 'allure-results/environment.properties'
    try:
        if not os.path.exists(properties_path):
            with open(properties_path, 'w') as properties:
                properties.write(f"URL = {os.getenv('ROOT_URL')}\n")
                properties.write(f"Browser = {os.getenv('BROWSER')}")
    except Exception as e:
        print(f"Error creating environment.properties: {e}")

def write_executor():
    executor_path = 'allure-results/executor.json'
    executor_data = {
    "name": os.getenv("EXECUTOR_NAME", "Unknown"),
    "buildName": os.getenv("EXECUTOR_BUILD_NAME", "Unknown"),
    }
    try:
        if not os.path.exists(executor_path):
            with open(executor_path, 'w') as executor_json:
                json.dump(executor_data, executor_json, indent=4)
        print(f"Executor information written to {executor_path}")
    except Exception as e:
        print(f"Error writing executor details: {e}")

def write_categories():
    categories_path = 'allure-results/categories.json'
    categories_data = [
        {
            "name": "Ignored tests",
            "messageRegex": ".*ignored.*",
            "matchedStatuses": ["skipped"],
            "flaky": True
        },
        {
            "name": "Infrastructure problems",
            "traceRegex": ".*RuntimeException.*",
            "matchedStatuses": ["broken", "failed"]
        },
        {
            "name": "Outdated tests",
            "messageRegex": ".*FileNotFound.*",
            "matchedStatuses": ["broken"]
        },
        {
            "name": "Passed",
            "messageRegex": ".*",
            "matchedStatuses": ["passed"]
        }
    ]

    try:
        if not os.path.exists(categories_path):
            with open(categories_path, 'w') as categories_json:
                json.dump(categories_data, categories_json, indent=4)
        print(f"Categories information written to {categories_path}")
    except Exception as e:
        print(f"Error writing categories: {e}")
