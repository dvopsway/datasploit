dataSploit as a Framework / Tool
================================

dataSploit is now available as a framework and can be used in 2 ways, either as a library such that it can be incorporated into other projects or as a standalone tool. Given below are the methods to install and use dataSploit in the mentioned 2 ways.

## 1. Set it up as a Library

dataSploit is now available on the [pypi repository](https://pypi.python.org/pypi/datasploit) for easy installation using pip. If you're a developer looking for a way to leverage the capabilities of dataSploit in your own projects, this method is probably the way to go for you. To use dataSploit as a library to incorporate in your own projects, please follow the below instructions to set it up.

```bash
# pip install datasploit
```

This command does all the work for you. It even installs the dependencies for dataSploit in your python environment. Once dataSploit is installed successfully, you need to edit the config file to add your own API keys. Simply run the below command to open up the config file in a vi editor. The below command is the gateway to edit the config file.

```bash
# datasploit_config
```

Now dataSploit is ready and can be used in any python project as a library. Following is a sample code:

```python
>>> import datasploit
>>> data = datasploit.username.username_gitscrape.main("username")
>>> datasploit.username.username_gitscrape.output(data)
[+] Found 1 repos for username

1. Username/TestData (3 commits)
        0913e1678e94456487c4c67288714511cbf2f9db
        0f67ed38c0cd2e87f508724b9744932db3e8c6ac
        b22997c0a4eb09a2b177ace811e55bea3b006df8

>>> from datasploit.emails import email_basic_checks
>>> data = email_basic_checks.main("info@google.com")
>>> print data
{u'free': False, u'domain': u'google.com', u'disposable': False, u'format_valid': True, u'did_you_mean': u'', u'catch_all': None, u'score': 0.8, u'role': True, u'user': u'info', u'smtp_check': True, u'email': u'info@google.com', u'mx_found': True}
>>> email_basic_checks.output(data)
Is it a free Email Address?: No
Email ID Exist?:  Yes
Can this domain recieve emails?:  Yes
Is it a Disposable email?:  No
```

## 2. Set it up as a Standalone Tool

If you're looking to use dataSploit quickly for scavenging information, you can simply run it as a standalone tool. Follow the below commands to set it up.

```bash
# git clone https://github.com/datasploit/datasploit /etc/datasploit
# cd /etc/datasploit/
# pip install -r requirements.txt
# mv config_sample.py config.py
# vi config.py
```

The steps mentioned above are all that is required to get dataSploit up and running. Once done, following is the sample usage of different modules or dataSploit as a whole.

```bash
# python datasploit.py test.com
           ____/ /____ _ / /_ ____ _ _____ ____   / /____   (_)/ /_
          / __  // __ `// __// __ `// ___// __ \ / // __ \ / // __/
         / /_/ // /_/ // /_ / /_/ /(__  )/ /_/ // // /_/ // // /_
         \__,_/ \__,_/ \__/ \__,_//____// .___//_/ \____//_/ \__/
                                       /_/

                    Open Source Assistant for #OSINT
                      Website: www.datasploit.info

User Input: test.com
Looks like a DOMAIN, running domainOsint...

---> Trying luck with PunkSpider

[-] No Vulnerabilities found on PunkSpider


---> Harvesting Email Addresses:.

sales@test.com
john.test@test.com
recipient@test.com
alice@test.com
someone@test.com
anonymous@test.com
sample@test.com
...


# python emails/email_basic_checks.py info@google.com

---> Basic Email Check(s)..

Is it a free Email Address?: No
Email ID Exist?:  Yes
Can this domain recieve emails?:  Yes
Is it a Disposable email?:  No

# python username/username_gitscrape.py username

[+] Scraping Git for Repos and Commits

[+] Found 1 repos for username username

1. KunalAggarwal/TestData (3 commits)
        0913e1678e94456487c4c67288714511cbf2f9db
        0f67ed38c0cd2e87f508724b9744932db3e8c6ac
        b22997c0a4eb09a2b177ace811e55bea3b006df8

```

That's it. dataSploit is now setup and ready to go. Both methods of installation provide flexibilty to all types of users to leverage the modules of dataSploit as needed.  
