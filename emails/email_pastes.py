#!/usr/bin/env python

import base
import config as cfg
import requests
import json
import sys
import re
from termcolor import colored

ENABLED = True


class style:
    BOLD = '\033[1m'
    END = '\033[0m'


def colorize(string):
    colourFormat = '\033[{0}m'
    colourStr = colourFormat.format(32)
    resetStr = colourFormat.format(0)
    lastMatch = 0
    formattedText = ''
    for match in re.finditer(
            r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})|/(?:http:\/\/)?(?:([^.]+)\.)?datasploit\.info/|/(?:http:\/\/)?(?:([^.]+)\.)?(?:([^.]+)\.)?datasploit\.info/)',
            string):
        start, end = match.span()
        formattedText += string[lastMatch: start]
        formattedText += colourStr
        formattedText += string[start: end]
        formattedText += resetStr
        lastMatch = end
    formattedText += string[lastMatch:]
    return formattedText


def google_search(email):
    url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=\"%s\"&start=1" % (
        cfg.google_cse_key, cfg.google_cse_cx, email)
    all_results = []
    r = requests.get(url)
    data = json.loads(r.content)
    if int(data['searchInformation']['totalResults']) > 0:
        all_results += data['items']
        while "nextPage" in data['queries']:
            next_index = data['queries']['nextPage'][0]['startIndex']
            url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=\"%s\"&start=%s" % (
                cfg.google_cse_key, cfg.google_cse_cx, email, next_index)
            data = json.loads(requests.get(url).content)
            all_results += data['items']
    return all_results


def banner():
    print colored(style.BOLD + '\n---> Finding Paste(s)..\n' + style.END, 'blue')


def main(email):
    if cfg.google_cse_key != "" and cfg.google_cse_key != "XYZ" and cfg.google_cse_cx != "" and cfg.google_cse_cx != "XYZ":
        data = google_search(email)
        return data
    else:
        return "INVALID_API"


def output(data, email=""):
    if data == "INVALID_API":
        print colored(
            style.BOLD + '\n[-] google_cse_key and google_cse_cx not configured. Skipping paste(s) search.\nPlease refer to http://datasploit.readthedocs.io/en/latest/apiGeneration/.\n' + style.END,
            'red')
    else:
        print "[+] %s results found\n" % len(data)
        for x in data:
            print "Title: %s\nURL: %s\nSnippet: %s\n" % (x['title'], colorize(x['link']), colorize(x['snippet']))


if __name__ == "__main__":
    try:
        email = sys.argv[1]
        banner()
        result = main(email)
        output(result, email)
    except Exception as e:
        print e
        print "Please provide an email as argument"
