# sauce-demo
Python-behave regression test framework for user journeys at https://www.saucedemo.com

## Setup checklist

* [Clone the repository](https://github.com/GitMe23/sauce-demo.git#clone-the-repository)
* [Download Chrome](https://github.com/GitMe23/sauce-demo.git#download-chrome)
* [Download Python 3](https://github.com/GitMe23/sauce-demo.git#download-python-3)
* [Install requirements](https://github.com/GitMe23/sauce-demo.git#install-requirements)
* [Run the test scenarios](https://github.com/GitMe23/sauce-demo.git#run-the-test-scenarios)
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
python3 -m pip install -r requirements.txt
```

### Run the test scenarios
Once you have the repo, Chrome, Python 3 and have installed the requirements, simply run the following from the same directory:
```bash
behave
```

> ## Note on security
>The [.env](.env) file loads environment variables such as credentials, addresses and environment variables of the system under test.
>This is prepopulated with the example login credentials for demonstration. 
>Passwords would typically be populated locally before running the framework, for example, by using:
>```bash
>export SAUCE_PASSWORD="secret_sauce"
>```

