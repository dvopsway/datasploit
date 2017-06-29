#!/usr/bin/env python

import base
import config as cfg
import requests
import json
import sys
from termcolor import colored
import time

ENABLED = True


class style:
    BOLD = '\033[1m'
    END = '\033[0m'


def shodandomainsearch(domain):
    time.sleep(0.3)
    endpoint = "https://api.shodan.io/shodan/host/search?key=%s&query=hostname:%s&facets={facets}" % (
    cfg.shodan_api, domain)
    req = requests.get(endpoint)
    return req.content


def banner():
    print colored(style.BOLD + '\n---> Searching in Shodan:\n' + style.END, 'blue')


def main(domain):
    return json.loads(shodandomainsearch(domain))


def output(data, domain=""):
    if 'matches' in data.keys():
        for x in data['matches']:
            print "IP: %s\nHosts: %s\nDomain: %s\nPort: %s\nData: %s\nLocation: %s\n" % (
            x['ip_str'], x['hostnames'], x['domains'], x['port'], x['data'].replace("\n", ""), x['location'])
    print "-----------------------------\n"


if __name__ == "__main__":
    try:
        domain = sys.argv[1]
        banner()
        result = main(domain)
        output(result, domain)
    except Exception as e:
        print e
        print "Please provide a domain name as argument"
