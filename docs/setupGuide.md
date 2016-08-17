This page holds the setup guide you will need before kicking off the datasploit in your system. Please note that all the documentation is as per *nix machines, and the tool has not been thoroughly tested on Windows platform. If you would like to volunteer for the same, give us a shout at helpme@datasploit.info. Following are the quick steps to get you going:

If you want to work with web GUI, follow the steps till 7. Otherwise, follow till 5th and you should be good to go. 

### Step 1 - Download DataSploit to your system.

You can either use the git command line tools using the following command:
```
git clone https://github.com/upgoingstar/datasploit.git
```
, or you can simply download the zip file *([link](https://github.com/upgoingstar/datasploit/archive/master.zip))* and extract the same using unzip.
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
### Step 4: Generate API Keys and paste inside config_sample.py

Generate API keys using the *api Key Generation* guide at 
> http://datasploit.readthedocs.io/en/latest/apiGeneration/ 

and enter the respective values in config.py file. Leave all other key value pairs blank.

### Step 5: Install MongoDB

Datasploit uses mongoDb in the backend and hence require a running instance of mongoDb in order to save and query data. Install the mongoDb database as per the instructions from the below mentioned site:
> https://docs.mongodb.com/manual/installation

Create a directory for storing the db files, and Start the mongoDb service with this database path:
```
mkdir datasploitDb
mongod --dbpath datasploitDb
```

### Step 6: Install RabitMQ
Install rabbitMq so that celery framework can work efficiently. Use the following link for download and install instructions:
> https://www.rabbitmq.com/download.html

Step 7: Start all services:
```
brew services restart mongodb 
brew services restart rabbitmq
C_FORCE_ROOT=root celery -A core worker -l info --concurrency 20       
python manage.py runserver 0.0.0.0:8000  
```

Congratulations, you are now good to go. Lets go ahead and run our automated script for OSINT on a domain. 
```
python domainOsint.py <domain_name>
```
