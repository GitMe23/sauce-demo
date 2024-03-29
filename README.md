# sauce-demo

A front-end Python automation framework for testing user journeys at https://www.saucedemo.com

This framework makes use of an example website to run BDD style scenarios via automation using Python and the following libraries:
* Selenium Web Driver
* Beautiful Soup
* Pandas
* Behave

The repo includes a feature file for test scenarios in Cucumber format, an underlying step definition file for executing the tests, and a utility layer made up of helper methods where I have included single-responsibility, reuseable functions. You will need a Gitbash or Unix based terminal before walking through the installation listed below.

## Setup checklist

* [Clone the repository](https://github.com/GitMe23/sauce-demo.git#clone-the-repository)
* [Download Chrome](https://github.com/GitMe23/sauce-demo.git#download-chrome)
* [Download Python 3](https://github.com/GitMe23/sauce-demo.git#download-python-3)
* [Install requirements](https://github.com/GitMe23/sauce-demo.git#install-requirements)
* [Run the test scenarios](https://github.com/GitMe23/sauce-demo.git#run-the-test-scenarios)
* [Optional: Reporting](https://github.com/GitMe23/sauce-demo.git#test-reports)
* [Note on security](https://github.com/GitMe23/sauce-demo.git#note-on-security)


### Clone the repository
```bash
git clone https://github.com/GitMe23/sauce-demo.git
```

### Download Chrome
Downloads found at https://www.google.com/intl/en_uk/chrome/dr/download/

### Python 3
Please ensure that Python 3 is installed on your machine. You can check in 
a bash shell or command prompt by running:
```bash
python3 --version
```
The downloads can be found at https://www.python.org/downloads/

### Install requirements
After installing the repo and Python 3, the required dependencies need to be installed within the project folder by running:
```bash
pip install -r requirements.txt
```
If you have trouble with pip or from pre-existing packages, try installing just within the module itself:
```bash
python3 -m pip install -r requirements.txt
```

### Run the test scenarios
Once you have the repo, Chrome, Python 3 and have installed the requirements, simply run the following from the same directory:
```bash
behave
```
The test framework should start running and you will see a web driver opening Chrome and automating tests.

### Test reports
###### -- OPTIONAL
By default, the test framework uses Behave's logger to print results in the console, and also write custom logging to logs/demo.log. If you would like to install a web app to open and view comprehensive test reports from within a browser, you will need to have npm installed and allure-behave.

Inside the repository folder:
```bash
npm install -g allure-commandline
```

```bash
python3 -m pip install allure-behave
```
You can also try:
```bash
pip install allure-behave
```

Then instead of 'behave', run the shell script from within the project directory:
```bash
./run_with_report.sh
```
The test framework should now run and your default browser will open a browser-based report.


> ## Note on security
>The [.env](.env) file loads environment variables such as credentials, addresses and environment variables of the system under test.
>This is prepopulated with the example login credentials for demonstration. 
>Passwords would typically be populated locally before running the framework, for example, by using:
>```bash
>export SAUCE_PASSWORD="secret_sauce"
>```

