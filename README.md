# OSINT for Penetration Testing

## Usage

```
python domainOsint.py <domain_name>
```
```
python git_searcher.py <git_username>
```
```
python emailOsint.py <emailId>
```

## SETUP and Contribution

### Config files

```
cp config_sample.py config.py
```
Then modify config.py with your API Keys

### Python dependencies

```
pip install -r requirements.txt
```

If you have updated the code and want to push the pip dependencies in the requirements.txt 

```
pip freeze > requirements.txt
```
Note: if you don't do this within virtual environment it will take list of all packages installed in system


### Virtual Environment setup

after first time clone you need to configure virtual environment
```
pip install virtualenv
```

Documentation 
http://docs.python-guide.org/en/latest/dev/virtualenvs/

Setup virtual environment for first time
```
virtualenv venv
```

Activate Virtual Environment
```
source venv/bin/activate
```

Deactivate
```
deactivate
```