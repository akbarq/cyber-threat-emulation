##################################################################
# Description: dga.py emulates DGA based malare traffic requests #                           
# Version: 1.0                                                   #
# Author: Akbar Qureshi                                          #
##################################################################

#!/usr/bin/env python3
import string
import random
import requests
import sys

if len(sys.argv) < 2:
    print ('Usage: dga.py number_of_dga_requests')
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
