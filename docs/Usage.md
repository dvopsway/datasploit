Datasploit allows you to perform OSINT on a domain_name, email_id, username and phoneNumber. In order to launch any script, lets first understand the nomenclature of these scripts:

* All the scripts meant to perform osint on domain starts with the keyword ***'domain_'***. Eg. domain_subdomains, domain_whois, etc. In similar manner, scripts for osint on email_id starts with ***'email_'***, eg. email_fullcontact. 
* Scripts with an *underscore* are standalone scripts and collects data of one specific kind. 
* Scripts without an underscore are the ones used for automated collection of data using standalone scripts. Eg. domainOsint.py

In order to run any script, pass the respective argument. For example, domainOsint and domain_subdomains.py will expect a domain name to be passed.
```
python domainOsint.py -d example.com
python domain_subdomains.py example.com
```
While, domainOsint will call all other domain_* scripts and list down data as well as dump the same in mongoDb, domain_subdomains and other such scripts will just list down data specific to their function. 

domainOsint.py generates a JSON and an HTML report in reports folder as following hirarchy (example files are based on abcd.com domain)

../datasploit/reports

---------------------|------abcd.com

---------------------|------|------abcd.com_YYYY-MM-DD-HH-MM-SS.html

---------------------|------|------abcd.com_YYYY-MM-DD-HH-MM-SS.json

---------------------|------|------abcd.com_YYYY-MM-DD-HH-MM-SS.subdomains.txt

---------------------|------|------abcd.com_YYYY-MM-DD-HH-MM-SS.emails.txt



