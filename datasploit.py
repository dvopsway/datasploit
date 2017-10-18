#!/usr/bin/env python

import re
import sys
import textwrap
import argparse
import emailOsint
import domainOsint
import ipOsint
import usernameOsint
from tld import get_tld
from netaddr import IPAddress,AddrFormatError


def main(argv):
    output=None
    desc="""                                                           
   ____/ /____ _ / /_ ____ _ _____ ____   / /____   (_)/ /_
  / __  // __ `// __// __ `// ___// __ \ / // __ \ / // __/
 / /_/ // /_/ // /_ / /_/ /(__  )/ /_/ // // /_/ // // /_  
 \__,_/ \__,_/ \__/ \__,_//____// .___//_/ \____//_/ \__/  
                               /_/                         
                                                           
            Open Source Assistant for #OSINT               
                www.datasploit.info                                                           

    """
    epilog="""              Connect at Social Media: @datasploit                  
                """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description=textwrap.dedent(desc),epilog=epilog)
    parser.add_argument("-i","--input",help="Provide Input",dest='target',required=True)
    parser.add_argument("-a","--active",help="Run Active Scan attacks",dest='active',action="store_false")
    parser.add_argument("-q","--quiet",help="Run scans in automated manner accepting default answers",dest='quiet',action="store_false")
    parser.add_argument("-o","--output",help="Provide Destination Directory",dest='output')
    if len(argv) == 0:
        parser.print_help()
        sys.exit()
    x=parser.parse_args()
    active=x.active
    quiet=x.quiet
    user_input=x.target
    output=x.output
    print textwrap.dedent(desc)
    try:    
        print "User Input: %s" % user_input
        try:
            inp=IPAddress(user_input);
            if inp.is_private() or inp.is_loopback():
                print "Internal IP Detected : Skipping"
                sys.exit()
            else:
                print "Looks like an IP, running ipOsint...\n"
                ipOsint.run(user_input, output)
        except SystemExit:
            print "exiting"
        except AddrFormatError:
            if re.match('[^@]+@[^@]+\.[^@]+', user_input):
                print "Looks like an EMAIL, running emailOsint...\n"
                emailOsint.run(user_input, output)
            elif get_tld(user_input, fix_protocol=True,fail_silently=True) is not None:
                print "Looks like a DOMAIN, running domainOsint...\n"
                domainOsint.run(user_input, output)
            else:
                print "Nothing Matched assuming username, running usernameOsint...\n"
                usernameOsint.run(user_input, output)
        except:
            print "Unknown Error Occured"
    except KeyboardInterrupt:
        print "Ctrl+C called Quiting"

if __name__ == "__main__":
   main(sys.argv[1:])