# sauce-demo
Python-behave regression test framework targeting user journeys on the sauce demo website

## Installation
Python 3
Install Requirements via requirements.txt

## Requirements
After installing Python 3, all of the dependencies can be installed by running:
```bash
python3 -m pip install -r requirements.txt
```

## Environment details
The .env is used for environment variables such as the test environment.
The .env file in this project handles the example password. 
Ordinarily, credentials would not exist in 
the test framework and be populated locally using:
```bash
export SAUCE_PASSWORD="secret_sauce"
```
