#!/bin/bash

echo "Running Python-behave test automation framework..."
echo "This may take a couple of minutes"
echo "See README for instructions on installation"

behave -f allure_behave.formatter:AllureFormatter -o allure-results features/demo.feature
allure serve allure-results/
