# sauce-demo
Python-behave regression test framework targeting user journeys on the [sauce demo website]([url](https://www.saucedemo.com))

## Setup checklist

* [Clone the repository](https://github.com/GitMe23/sauce-demo.git#clone-the-repository)
* [Download Chrome](https://github.com/GitMe23/sauce-demo.git#download-chrome)
* [Download Python 3](https://github.com/GitMe23/sauce-demo.git#download-python-3)
* [Install requirements](https://github.com/GitMe23/sauce-demo.git#install-requirements)
* [Run the test scenarios](https://github.com/GitMe23/sauce-demo.git#run-the-test-scenarios)
* [Note on security](https://github.com/GitMe23/sauce-demo.git#note-on-security)

You may also like to download a Cucumber plug-in if running this repo in an IDE, to make use of syntax highlighting:

![Cucumber syntax highlighting](https://private-user-images.githubusercontent.com/105940138/298312357-dcefc36b-66a1-4ef7-a9c2-3c4d6e713fd9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDU3OTM0NTEsIm5iZiI6MTcwNTc5MzE1MSwicGF0aCI6Ii8xMDU5NDAxMzgvMjk4MzEyMzU3LWRjZWZjMzZiLTY2YTEtNGVmNy1hOWMyLTNjNGQ2ZTcxM2ZkOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMTIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDEyMFQyMzI1NTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mNTBkZDE2OTEyOGI3NDdiMjk0NmZkN2U3NzM4YTA4NGQyN2YwNTVkOWQ5ZTY4MDNmNTRjNTU4ZWZmMzkxZDc2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.toXNmTDqqSQCJFwIMnekDlaI0UwP2-CQZ0vqhlqwbjU)


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

