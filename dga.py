#!/usr/bin/python3
import string
import random
import requests
import sys

#############################################################
# Description: dga.py tries to emulate malware DGA requests #                           
# Version: 1.0                                              #
# Author: Akbar Qureshi                                     #
#############################################################

if len(sys.argv) < 2:
    print ('Usage: dga.py dga_requests')
    print ('Example: dga.py 5') 
    sys.exit(1)

for dga in range(int(sys.argv[1])):
        dga = (''.join(random.choice(string.ascii_lowercase) for i in range(12)))
        tlds = ['cc', 'top', 'ws', 'to', 'so', 'gq', 'gdn', 'cf']
        tld = '{}.{}'.format(dga,random.choice(tlds))
        print(tld)
        try:
            requests.get('http://{}'.format(tld))
        except:
                pass
