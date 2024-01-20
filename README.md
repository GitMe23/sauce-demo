# sauce-demo
Python-behave regression test framework targeting user journeys on the sauce demo website



### Clone the repository
```bash
git clone https://github.com/GitMe23/sauce-demo.git
```

### Installation
Please nesure that Python 3 is installed on your machine. You can check in 
a bash shell or command prompt by running:
```bash
python3 --version
```
The downloads can be found at https://www.python.org/downloads/

### Requirements
After installing Python 3, the required dependencies can be installed by running:
```bash
python3 -m pip install -r requirements.txt
```

### Running the tests
Once you have Python 3 and have installed the requirements, you can change directory in to the root folder and run the entire test framework by using:
```bash
behave
```

### Environment
The .env is used for environment variables such as credentials and details of the system under test.
The .env file in this project handles this and is prepopulated for demonstration. 
Credentials would typically be populated locally using:
```bash
export SAUCE_PASSWORD="secret_sauce"
```
