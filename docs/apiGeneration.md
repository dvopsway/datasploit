We need following API keys to run this tool efficiently:

shodan_api, censysio_id, censysio_secret, zoomeyeuser, zoomeyepass, clearbit_apikey, emailhunter, fullcontact, google_cse_key, google_cse_cx.

## Shodan_api
* [Register](https://account.shodan.io/register) an account in shodan.
* Visit your registered email id and activate the account.
* [Login](https://account.shodan.io/login) to your account and you will find the API keys under profile overview tab.
* Copy the API key and this is the value for *shodan_api* field in the config.py file. 

## Censysio ID and Secret
* [Register](https://www.censys.io/register) an account in censysio.
* Visit your registered email id and activate the account.
* [Login](https://www.censys.io/login) to your account.
* Visit [Account](https://www.censys.io/account) tab to get API ID and Secret.
* Your API key is the value for *censysio_id* field and API Secret is the value for *censysio_secret* field in config.py file.

## Clearbit API
* [Register](https://dashboard.clearbit.com/signup) an account in clearbit.
* It will auto redirect to the account.
* Visit [API keys](https://dashboard.clearbit.com/keys) tab to get API key.
* Copy the API key and this is the value for *clearbit_apikey* field in the config.py file. 

## Emailhunter API
* [Register](https://emailhunter.co/users/sign_up) an account in emailhunter.
* Click on activation link send to your registered email address and it will auto redirect to the account.
* Visit [API keys](https://emailhunter.co/api_keys) tab to get API key.
* Copy the API key and this is the value for *emailhunter* field in the config.py file. 

## Fullcontact API
* [Register](https://portal.fullcontact.com/signup) an account in fullcontact.
* [Login](https://portal.fullcontact.com/signin/).
* It will ask for mobile number verification, complete that.
* You will be redirected to the page where you can get the API key.
* Additionally you will also get one email in the registered email id with API details.
* Copy the API key and this is the value for *fullcontact_api* field in the config.py file. 


## Google Custom Search Engine API key and CX id
* Go to https://console.developers.google.com/ > Credentials
* Click on 'Create Credentials' and select API key. 
* Click on restrict key. 
* Select HTTP Headers (Websites) radio button.
* Add **.datasploit.info/\** in restrictions. This is done in order to stop unintentional usage of your api key. 
* Copy the API key and click on save button. This is the value for *google_cse_key* field in the config.py file. 
* Go to https://cse.google.com/cse/all, Click on Add button. 
* In sites to search box, enter "pastebin.com" and "pastie.org"
* Give any name to your search engine and click on Create button. 
* Go to https://cse.google.com/cse/all again and click on the search engine you just created. 
* Click on the 'Search engine id' button and copy your search engine id. This is the value for *google_cse_cx* field in config.py file.


## Zoomeye Username and Password
* [Register](https://www.zoomeye.org/accounts/register) an user with zoomeye and use the credentials for this tool. (Don't worry if you are redirected to sso.telnet404.com. *This is how it works.)*
* Name of fields in the signup form -  *1. email, 2. username, 3. nickname, 4. password, 5. confirm_password, 6. captcha*
* Once you fill out the details it will redirect you to the account page.
* There you will found something: *(Status: Inactive. Activate Now)*
* Click on activate now and two fileds will be populated.
* The first field will be captcha and the second one will be email id.
* Once you fill the email id in the second text box, click on send activation code.
* Check the activation code your email account.
* Put this activation code in the email id text box and click on determine.
* Now your account is activated and use those credentials in the tool.
* Email ID which you have used to sign up is your username and is the value for *zoomeyeuser* field in config.py
* Your account password is the value for *zoomeyepass* field in the config.py
