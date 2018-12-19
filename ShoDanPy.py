#!/usr/bin/python

import shodan
import json
import sys
import MySQLdb

from ShodanSearch import ShodanSearch


# Setup of API key
with open("api.key","r") as f:
    apiKey = f.read().replace("\n","")

# take IP from first arg
ip = sys.argv[1]
#Call function
print(ShodanSearch(apiKey,ip))
