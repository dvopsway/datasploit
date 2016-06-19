# Overview of the tool:
* Performs OSINT on a domain / email / username / phone and find out information from different sources.
* Correlates and collaborate the results, show them in a consolidated manner. 
* Tries to find out credentials, api-keys, tokens, subdomains, domain history, legacy portals, etc. related to the target. 
* Use specific script / launch automated OSINT for consolidated data.
* Available in both GUI and Console.
 
Following API configs are mandatory for proper results in domainOsint.py:
* shodan_api
* censysio_id
* censysio_secret
* zoomeyeuser
* zoomeyepass
* clearbit_apikey
* emailhunter

Other modules:
* github_access_token
* instagram_token
* instagram_client_id
* instagram_client_secret
* jsonwhois

*We are working towards few sample API keys which we can deliver as part of the project so new users can quickly evaluate the tool. Although those will help only in evaluating as al evaluations will go with these keys and hence more chances of hitting the rate limiting on them.  *

## Usage
All the files starting with domain_ requires a domain name to be passed as first argument. Same follows for email, etc. 

```
python domain_subdomain.py <domain_name>
```

To launch an automated OSINT on domain, shoot following query:

```
python domainOsint.py <domain_name>
```

## SETUP and Contribution
* Change config_sample.py to config.py
```
mv config_sample.py config.py
```
* Configure respective API keys. Documentation for generating these keys will be shared very shortly. Believe us, we are working hard to get things in place. 
* Sources for which API keys are missing, will be simply skipped for the search. 

### Config files


### Python dependencies

```
pip install -r requirements.txt
```

If you have updated the code and want to push the pip dependencies in the requirements.txt 

```
pip freeze > requirements.txt
```


# Note
```
Currently project is in developement phase and lot of work is going on. Custom error handling is also not implemented, and all the focus is to create required functionality. 
```
