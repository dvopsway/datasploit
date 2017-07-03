#!/usr/bin/env python

import re
import sys
import optparse
import emailOsint
import domainOsint
import ipOsint
import usernameOsint

parser = optparse.OptionParser()
parser.add_option('-a', '--active', action="store", dest="domain", help="Launches Active Scans (work in progress)",
                  default="spam")
options, args = parser.parse_args()


def printart():
    print "\t                                                           "
    print "\t   ____/ /____ _ / /_ ____ _ _____ ____   / /____   (_)/ /_"
    print "\t  / __  // __ `// __// __ `// ___// __ \ / // __ \ / // __/"
    print "\t / /_/ // /_/ // /_ / /_/ /(__  )/ /_/ // // /_/ // // /_  "
    print "\t \__,_/ \__,_/ \__/ \__,_//____// .___//_/ \____//_/ \__/  "
    print "\t                               /_/                         "
    print "\t                                                           "
    print "\t            Open Source Assistant for #OSINT               "
    print "\t              Website: www.datasploit.info                 "
    print "\t                                                           "


def main(user_input):
    printart()
    print "User Input: %s" % user_input

    if re.match('[^@]+@[^@]+\.[^@]+', user_input):
        print "Looks like an EMAIL, running emailOsint...\n"
        emailOsint.run(user_input)
    elif re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', user_input):
        print "Looks like an IP, running ipOsint...\n"
        ipOsint.run(user_input)
    elif re.match('^[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63}).$', user_input):
        print "Looks like a DOMAIN, running domainOsint...\n"
        domainOsint.run(user_input)
    else:
        print "Looks like a Username, running usernameOsint...\n"
        usernameOsint.run(user_input)


if __name__ == "__main__":
    try:
        user_input = sys.argv[1]
    except:
        print "\n[-] Invalid Input. Exiting now..\n"
        sys.exit(0)
    main(user_input)
