This page holds the setup guide you will need before kicking off the datasploit in your system. Please note that all the documentation is as per *nix machines, and the tool has not been thoroughly tested on Windows platform. If you would like to volunteer for the same, give us a shout at helpme@datasploit.info. Following are the quick steps to get you going:

If you want to work with web gui, follow the steps till 7. Otherwise, follow till 5th and you should be good to go. 

### Step 1 - Download DataSploit to your system.

You can either use the git command line tools using the following command:
```
git clone https://github.com/datasploit/datasploit.git
```
, or you can simply download the zip file *([link](https://github.com/datasploit/datasploit/archive/master.zip))* and extract the same using unzip.
```
unzip master.zip
```

### Step 2: Install python dependencies

Go into the tool directory and install all the python libraries using the requirements.txt file. In case you encounter 'Permission Denied' error, use sudo.
```
cd master
pip install -r requirements.txt
```
### Step 3: Rename config_sample.py to config.py

Please make sure that config.py is added in your gitIgnore file so that this is not commited in any case. We care for your data too, and hence this tip. :) 
```
mv config_sample.py config.py
```
### Step 4: Generate API Keys and paste inside config.py

Generate API keys using the *api Key Generation* guide at 
> http://datasploit.readthedocs.io/en/latest/apiGeneration/ 

and enter the respective values in config.py file. Leave all other key value pairs blank.

Congratulations, you are now good to go. Lets go ahead and run our automated script for OSINT on a domain. 
```
python domainOsint.py -d <domain_name>
```
