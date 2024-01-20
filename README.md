# sauce-demo
Python-behave regression test framework targeting user journeys on the sauce demo website

## Tools
If you haven't already, you will need to have the following installed locally in order to run the test framework:

* [Clone the repository](https://github.com/GitMe23/sauce-demo.git#clone-the-repository)
* [Chrome web browser](https://github.com/GitMe23/sauce-demo.git#chrome-web-browser)
* [Python 3](https://github.com/GitMe23/sauce-demo.git#python-3)
* [Requirements](https://github.com/GitMe23/sauce-demo.git#requirements)

Also see:

* [Running the test scenarios](https://github.com/GitMe23/sauce-demo.git#running-the-test-scenarios)
* [Note on security](https://github.com/GitMe23/sauce-demo.git#note-on-environment)



### Clone the repository
```bash
git clone https://github.com/GitMe23/sauce-demo.git
```

### Chrome web browser
Downloads found at https://www.google.com/intl/en_uk/chrome/dr/download/

### Python 3
Please ensure that Python 3 is installed on your machine. You can check in 
a bash shell or command prompt by running:
```bash
python3 --version
```
The downloads can be found at https://www.python.org/downloads/

### Requirements
After installing the repo and Python 3, the required dependencies can be installed by running:
```bash
cd {path_to_sauce_demo}
python3 -m pip install -r requirements.txt
```

### Running the tests
Once you have the repo, Chrome, Python 3 and have installed the requirements, simply run the following from the same directory:
```bash
behave
```

> ### Note on environment
>The [.env](.env) file loads environment variables such as credentials, addresses and environment variables of the system under test.
>This is prepopulated with the example login credentials for demonstration. 
>Passwords would typically be populated locally before running the framework by using:
>```bash
>export SAUCE_PASSWORD="secret_sauce"
>```

