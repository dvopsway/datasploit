## Step 1 - Download DataSploit to your system.

**Method 1:** 
Using git command line (Make sure you have Git up and running in your system).
```
git clone https://github.com/upgoingstar/datasploit.git
```

**Method 2:** 
Download the zip file *([link](https://github.com/upgoingstar/datasploit/archive/master.zip))* and Extract the zip file.
```
wget https://github.com/upgoingstar/datasploit/archive/master.zip
unzip master.zip
```

## Step 2: Install python dependencies 
(Make sure pip is installed in your system).
```
cd master
pip install -r requirements.txt
```
## Step 3: Rename config_sample.py to configpy
```
mv config_sample.py config.py
```
## Step 4: Generate API Keys and paste inside config_sample.py.
* Generate respective API keys using step 4 and enter them in config.py file. 
* Help for generating required API keys: *([http://datasploit.readthedocs.io/en/latest/apiGeneration](http://datasploit.readthedocs.io/en/latest/apiGeneration/))*.

## Step 5: Install MongoDB
* Install mongoDB using the documentation - *([https://docs.mongodb.com/manual/installation](https://docs.mongodb.com/manual/installation/))* 
* Start the mongoDb service with a defined path after creating a data direcotry:
```
mkdir datasploitDb
mongod --dbpath datasploitDb
```
#### Step 6: Lanuch the tool.
```
python domainOsint.py <domain_name>
```
