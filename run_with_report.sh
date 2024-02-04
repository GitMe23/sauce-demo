#!/bin/bash

echo "Running Python-behave test automation framework..."
echo "See README for any troubleshooting"

mkdir -p allure-results/history
behave -f allure_behave.formatter:AllureFormatter -o allure-results features
cp allure-report/history/* allure-results/history
allure generate --clean allure-results
allure open


