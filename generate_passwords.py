#!/usr/bin/env python

import sys

combination = ["123@%s", "%s@123", "123%s", "%s123"]
email = sys.argv[1]

user = email.split("@")[0]
print 

for x in combination:
	print x % (user)
