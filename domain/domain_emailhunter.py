#!/usr/bin/env python

import base
import config as cfg
import requests
import json
import sys
import time
from termcolor import colored

ENABLED = True


class style:
    BOLD = '\033[1m'
    END = '\033[0m'


def emailhunter(domain):
    collected_emails = []
    time.sleep(0.3)
    url = "https://api.emailhunter.co/v1/search?api_key=%s&domain=%s" % (cfg.emailhunter, domain)
    res = requests.get(url)
    try:
        parsed = json.loads(res.text)
        if 'emails' in parsed.keys():
            for email in parsed['emails']:
                collected_emails.append(email['value'])
    except:
        print 'CAPTCHA has been implemented, skipping this for now.'
    return collected_emails


def banner():
    print colored(style.BOLD + '\n---> Harvesting Email Addresses:.\n' + style.END, 'blue')


def main(domain):
    if cfg.emailhunter != "" and cfg.emailhunter != "":
        return emailhunter(domain)


def output(data, domain=""):
    for x in data:
        print str(x)


if __name__ == "__main__":
    try:
        domain = sys.argv[1]
        banner()
        result = main(domain)
        output(result, domain)
    except Exception as e:
        print e
        print "Please provide a domain name as argument"
